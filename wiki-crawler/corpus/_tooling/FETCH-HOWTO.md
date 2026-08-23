# How to fetch HOI4 wiki pages (read this fully before starting)

You have a dedicated browser tab. Its numeric ID is given to you in your task prompt as `TABID`.

**Step 0 — always do this first:** call `mcp__claude-in-chrome__navigate` with
`{url: "https://hoi4.paradoxwikis.com/Hearts_of_Iron_4_Wiki", tabId: TABID}`. The fetch below needs
same-origin access to `/api.php`, and a tab sitting on `chrome://newtab` will fail. After that,
**never navigate the tab away** from `hoi4.paradoxwikis.com`.

The table converter below is colspan/rowspan-aware, so wiki tables with merged header cells (law
tables, balance-of-power tables) come out with correct column alignment. Still eyeball any table
whose header count looks off.

If a `browser_batch` call reports "failed in the extension", just re-issue the two actions as two
separate calls — it recovers. If a `get_page_text` result is too large for one tool result, the
harness writes it to a file on disk and tells you the path; read that file rather than re-fetching.

## The loop

For each batch of 1–4 wiki pages, make ONE `mcp__claude-in-chrome__browser_batch` call containing
two actions:

1. `javascript_tool` — fetches the pages via the MediaWiki API, converts the rendered HTML to
   markdown, and dumps the result into the DOM. Returns only `LEN=<chars>`.
2. `get_page_text` — reads the dumped markdown back out in full.

Then write the distilled result to a `.md` file with a bash heredoc.

**Keep each batch under ~60000 characters of output.** If `LEN=` comes back above ~70000, re-run
with fewer titles. Big pages (national focus trees, country pages, `Land units`, `Ship`,
`Equipment`, `List of states`) should be fetched ONE at a time.

## The javascript_tool payload

Set `action: "javascript_exec"`, `tabId: TABID`, and `text` to exactly this, changing only the
`titles` array on the second-to-last line:

```javascript
function h2md(html){const doc=new DOMParser().parseFromString(html,'text/html');const root=doc.body;root.querySelectorAll('style,script,.mw-editsection,.navbox,.toc,#toc,sup.reference,.thumb,.mw-references-wrap,.metadata,.ambox,.hatnote,.mw-empty-elt').forEach(e=>e.remove());root.querySelectorAll('img').forEach(im=>{const a=(im.getAttribute('alt')||'').trim();im.replaceWith(doc.createTextNode(a?('['+a+']'):''));});const clean=s=>(s||'').replace(/ /g,' ').replace(/\s+/g,' ').trim();const inline=el=>clean(el.textContent);function tb2md(tb){const rows=[...tb.querySelectorAll(':scope>tr,:scope>thead>tr,:scope>tbody>tr,:scope>tfoot>tr')];if(!rows.length)return '';const g=[];rows.forEach((tr,ri)=>{if(!g[ri])g[ri]=[];let ci=0;for(const c of [...tr.children].filter(c=>/^t[hd]$/i.test(c.tagName))){while(g[ri][ci]!==undefined)ci++;const cs=parseInt(c.getAttribute('colspan')||'1',10)||1;const rs=parseInt(c.getAttribute('rowspan')||'1',10)||1;const v=inline(c).replace(/\|/g,'/');for(let r=0;r<rs;r++){if(!g[ri+r])g[ri+r]=[];for(let k=0;k<cs;k++){g[ri+r][ci+k]=v;}}ci+=cs;}});const w=Math.max(...g.map(r=>r.length));const out=[];g.forEach((r,i)=>{const vals=[];for(let k=0;k<w;k++)vals.push(r[k]===undefined?'':r[k]);out.push('| '+vals.join(' | ')+' |');if(i===0)out.push('|'+vals.map(()=>'---').join('|')+'|');});return out.join('\n');}const parts=[];(function walk(node){for(const el of node.children){const tag=el.tagName.toLowerCase();if(/^h[1-6]$/.test(tag)){parts.push('\n'+'#'.repeat(Math.min(+tag[1],6))+' '+inline(el)+'\n');}else if(tag==='p'){const t=inline(el);if(t)parts.push(t+'\n');}else if(tag==='ul'||tag==='ol'){[...el.querySelectorAll(':scope>li')].forEach((li,i)=>{const t=inline(li);if(t)parts.push((tag==='ul'?'- ':(i+1)+'. ')+t);});parts.push('');}else if(tag==='dl'){[...el.children].forEach(d=>{const t=inline(d);if(t)parts.push(d.tagName==='DT'?('**'+t+'**'):('  '+t));});parts.push('');}else if(tag==='table'){const t=tb2md(el);if(t)parts.push('\n'+t+'\n');}else if(['div','section','center','blockquote'].includes(tag)){walk(el);}else{const t=inline(el);if(t&&t.length<6000)parts.push(t);}}})(root);return parts.join('\n').replace(/\n{3,}/g,'\n\n').trim();}
async function getpage(t){const r=await fetch('/api.php?action=parse&page='+encodeURIComponent(t)+'&prop=text&format=json&redirects=1');const j=await r.json();if(j.error)return '\n\n===== PAGE: '+t+' (ERROR '+j.error.code+') =====\n';return '\n\n===== PAGE: '+j.parse.title+' =====\n'+h2md(j.parse.text['*']);}
const titles=['Division','Combat tactics'];
let out='';for(const t of titles){out+=await getpage(t);}
document.body.innerHTML='<article id="dump"><pre style="white-space:pre-wrap"></pre></article>';document.querySelector('#dump pre').textContent=out;'LEN='+out.length;
```

Page titles use spaces (not underscores) and are case-sensitive after the first letter.
`&redirects=1` means redirects resolve automatically. A missing page returns
`(ERROR missingtitle)` — note it and move on; do not retry more than once.

## Finding page titles you weren't given

Same tab, same trick — this returns a list instead of page content:

```javascript
const j=await (await fetch('/api.php?action=query&list=search&srsearch=YOUR+QUERY&srlimit=30&format=json')).json();
const out=j.query.search.map(s=>s.title).join(' | ');
document.body.innerHTML='<article id="dump"><pre></pre></article>';document.querySelector('#dump pre').textContent=out;'LEN='+out.length;
```

or, for everything in a category:

```javascript
const j=await (await fetch('/api.php?action=query&list=categorymembers&cmtitle=Category:Achievements&cmlimit=500&cmnamespace=0&format=json')).json();
const out=j.query.categorymembers.map(s=>s.title).join(' | ');
document.body.innerHTML='<article id="dump"><pre></pre></article>';document.querySelector('#dump pre').textContent=out;'LEN='+out.length;
```

## If the browser tools are unavailable to you

Call `ToolSearch` with `select:mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text`
first. Only if that still fails, fall back to `WebFetch` on
`https://hoi4.paradoxwikis.com/<Page_Title>` with a data-extraction prompt (WebFetch is rate
limited — wait 60s between calls after a 429, and it refuses "reproduce verbatim" phrasing, so ask
it to "extract the game data as a structured markdown table").
