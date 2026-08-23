"""Fetch and markdown-convert Hearts of Iron 4 wiki pages.

hoi4.paradoxwikis.com sits behind a Fastly "Client Challenge" (a JS proof-of-work
gate) that blocks plain HTTP clients (requests, pymediawiki) entirely -- every
response, including robots.txt, comes back as challenge HTML instead of content.
A real browser passes the challenge automatically because it can execute the JS.

This module drives headless Chromium via Playwright to load the wiki once (which
passes the challenge and sets the session cookie), then uses the page's own
same-origin `fetch()` to call the MediaWiki API directly -- same trick used
previously via an interactive claude-in-chrome browser tab, just automated here.

Usage:
    uv run python -m hoi_wiki_crawler.fetch "Naval battle" "Ship designer"

Prints one "===== PAGE: <title> =====" block per page to stdout, with rendered
HTML converted to markdown (colspan/rowspan-aware tables, icons reduced to their
alt text). A missing page prints "(ERROR missingtitle)" for that title and moves
on to the rest.
"""

import sys

from playwright.sync_api import sync_playwright

WIKI_ENTRY_URL = "https://hoi4.paradoxwikis.com/Hearts_of_Iron_4_Wiki"

# Same html->markdown converter as hoi-wiki-agent-scrape-data/_tooling/FETCH-HOWTO.md,
# kept byte-for-byte identical so output matches the existing corpus. If you touch
# the extraction logic, update FETCH-HOWTO.md too so any browser-tab-driven agent
# stays consistent with this script.
_FETCH_PAGES_JS = r"""
async (titles) => {
  function h2md(html){const doc=new DOMParser().parseFromString(html,'text/html');const root=doc.body;root.querySelectorAll('style,script,.mw-editsection,.navbox,.toc,#toc,sup.reference,.thumb,.mw-references-wrap,.metadata,.ambox,.hatnote,.mw-empty-elt').forEach(e=>e.remove());root.querySelectorAll('img').forEach(im=>{const a=(im.getAttribute('alt')||'').trim();im.replaceWith(doc.createTextNode(a?('['+a+']'):''));});const clean=s=>(s||'').replace(/ /g,' ').replace(/\s+/g,' ').trim();const inline=el=>clean(el.textContent);function tb2md(tb){const rows=[...tb.querySelectorAll(':scope>tr,:scope>thead>tr,:scope>tbody>tr,:scope>tfoot>tr')];if(!rows.length)return '';const g=[];rows.forEach((tr,ri)=>{if(!g[ri])g[ri]=[];let ci=0;for(const c of [...tr.children].filter(c=>/^t[hd]$/i.test(c.tagName))){while(g[ri][ci]!==undefined)ci++;const cs=parseInt(c.getAttribute('colspan')||'1',10)||1;const rs=parseInt(c.getAttribute('rowspan')||'1',10)||1;const v=inline(c).replace(/\|/g,'/');for(let r=0;r<rs;r++){if(!g[ri+r])g[ri+r]=[];for(let k=0;k<cs;k++){g[ri+r][ci+k]=v;}}ci+=cs;}});const w=Math.max(...g.map(r=>r.length));const out=[];g.forEach((r,i)=>{const vals=[];for(let k=0;k<w;k++)vals.push(r[k]===undefined?'':r[k]);out.push('| '+vals.join(' | ')+' |');if(i===0)out.push('|'+vals.map(()=>'---').join('|')+'|');});return out.join('\n');}const parts=[];(function walk(node){for(const el of node.children){const tag=el.tagName.toLowerCase();if(/^h[1-6]$/.test(tag)){parts.push('\n'+'#'.repeat(Math.min(+tag[1],6))+' '+inline(el)+'\n');}else if(tag==='p'){const t=inline(el);if(t)parts.push(t+'\n');}else if(tag==='ul'||tag==='ol'){[...el.querySelectorAll(':scope>li')].forEach((li,i)=>{const t=inline(li);if(t)parts.push((tag==='ul'?'- ':(i+1)+'. ')+t);});parts.push('');}else if(tag==='dl'){[...el.children].forEach(d=>{const t=inline(d);if(t)parts.push(d.tagName==='DT'?('**'+t+'**'):('  '+t));});parts.push('');}else if(tag==='table'){const t=tb2md(el);if(t)parts.push('\n'+t+'\n');}else if(['div','section','center','blockquote'].includes(tag)){walk(el);}else{const t=inline(el);if(t&&t.length<6000)parts.push(t);}}})(root);return parts.join('\n').replace(/\n{3,}/g,'\n\n').trim();}
  async function getpage(t){const r=await fetch('/api.php?action=parse&page='+encodeURIComponent(t)+'&prop=text&format=json&redirects=1');const j=await r.json();if(j.error)return '\n\n===== PAGE: '+t+' (ERROR '+j.error.code+') =====\n';return '\n\n===== PAGE: '+j.parse.title+' =====\n'+h2md(j.parse.text['*']);}
  let out='';for(const t of titles){out+=await getpage(t);}
  return out;
}
"""

_SEARCH_JS = r"""
async (query) => {
  const j = await (await fetch('/api.php?action=query&list=search&srsearch=' + encodeURIComponent(query) + '&srlimit=30&format=json')).json();
  return j.query.search.map(s => s.title).join(' | ');
}
"""

_CATEGORY_JS = r"""
async (category) => {
  const j = await (await fetch('/api.php?action=query&list=categorymembers&cmtitle=' + encodeURIComponent(category) + '&cmlimit=500&cmnamespace=0&format=json')).json();
  return j.query.categorymembers.map(s => s.title).join(' | ');
}
"""


def fetch_pages(titles: list[str]) -> str:
    """Fetch one or more wiki pages, return concatenated markdown blocks."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(WIKI_ENTRY_URL, wait_until="networkidle", timeout=30000)
            if page.title() == "Client Challenge":
                raise RuntimeError(
                    "Fastly Client Challenge was not passed -- wiki returned the "
                    "challenge page instead of content."
                )
            return page.evaluate(_FETCH_PAGES_JS, titles)
        finally:
            browser.close()


def search_titles(query: str) -> str:
    """Search the wiki, return matching page titles joined by ' | '."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(WIKI_ENTRY_URL, wait_until="networkidle", timeout=30000)
            return page.evaluate(_SEARCH_JS, query)
        finally:
            browser.close()


def category_members(category: str) -> str:
    """List page titles in a wiki category (e.g. 'Category:Achievements')."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(WIKI_ENTRY_URL, wait_until="networkidle", timeout=30000)
            return page.evaluate(_CATEGORY_JS, category)
        finally:
            browser.close()


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: uv run python -m hoi_wiki_crawler.fetch <page title> [<page title> ...]",
            file=sys.stderr,
        )
        raise SystemExit(1)
    print(fetch_pages(sys.argv[1:]))


if __name__ == "__main__":
    main()
