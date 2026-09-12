#!/usr/bin/env python3
"""Publish pipeline: mirror the Obsidian vault into Quartz content/, and convert
Dataview blocks in Map notes into static link lists (Dataview only runs in Obsidian).

Usage: python3 publish.py            (uses default paths)
Then:  npx quartz build   (or the dev server auto-rebuilds)
"""
import os, re, glob, shutil, subprocess, sys
from pathlib import Path

def flatten_multicolumn():
    """Multi-Column-Markdown syntax only runs in Obsidian; on the site show sections stacked."""
    n=0
    for p in glob.glob(str(CONTENT/"**"/"*.md"), recursive=True):
        rp=Path(p); t=rp.read_text(encoding="utf-8")
        if "start-multi-column" not in t: continue
        t=re.sub(r"^--- start-multi-column:.*$","",t,flags=re.M)
        t=re.sub(r"^--- end-multi-column\s*$","",t,flags=re.M)
        t=re.sub(r"^--- column-break ---\s*$","",t,flags=re.M)
        t=re.sub(r"```column-settings\s*.*?```","",t,flags=re.S)
        rp.write_text(t,encoding="utf-8"); n+=1
    print(f"flattened multi-column in {n} files for the web")

def downscale_images():
    """Downscale published image copies to web size (vault keeps full-res)."""
    exts={".jpg",".jpeg",".png"}
    n=0
    for p in glob.glob(str(CONTENT/"attachments"/"*")):
        rp=Path(p)
        if rp.suffix.lower() not in exts: continue
        try:
            if rp.stat().st_size < 400_000: continue  # already small
            subprocess.run(["sips","-Z","1800","-s","formatOptions","80",str(rp)],
                           check=True, capture_output=True)
            n+=1
        except Exception:
            pass
    print(f"downscaled {n} images for the web")

VAULT = Path(os.path.expanduser("~/Obsidian/Mare-Nostrum"))
CONTENT = Path(os.path.expanduser("~/Obsidian/quartz-mare-nostrum/content"))

# 1) mirror vault -> content (exclude Obsidian internals, templates)
def mirror():
    if CONTENT.exists(): shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)
    excludes = {".obsidian","_templates",".git",".trash"}
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in excludes]
        rel = Path(root).relative_to(VAULT)
        for f in files:
            if f == ".DS_Store" or f == ".gitignore": continue
            dst = CONTENT/rel/f
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(Path(root)/f, dst)
    # landing page
    home = CONTENT/"Home.md"
    if home.exists(): shutil.copy2(home, CONTENT/"index.md")

# 2) index of every note's title + tags (for building lists)
def index_notes():
    notes=[]  # (title, tagset, relpath)
    for p in glob.glob(str(CONTENT/"**"/"*.md"), recursive=True):
        rp=Path(p)
        if rp.parent.name=="00-Maps" or rp.name in ("index.md","Home.md"): continue
        txt=rp.read_text(encoding="utf-8")
        m=re.search(r'^title:\s*"?(.*?)"?\s*$', txt, re.M)
        title=m.group(1) if m else rp.stem
        tm=re.search(r'^tags:\s*\[(.*?)\]', txt, re.M)
        tags=set()
        if tm:
            tags={t.strip().strip('"').lower() for t in tm.group(1).split(",") if t.strip()}
        notes.append((title, tags, rp))
    return notes

def de_dataview(notes):
    maps=glob.glob(str(CONTENT/"00-Maps"/"*.md"))
    for mp in maps:
        p=Path(mp); txt=p.read_text(encoding="utf-8")
        block=re.search(r"```dataview\s*(.*?)```", txt, re.S)
        if not block: continue
        query=block.group(1)
        folders=re.findall(r'from\s+"([^"]+)"', query) + re.findall(r'"([^"]+)"', query)
        tags=[t.lower() for t in re.findall(r'#([\w/-]+)', query)]
        chosen=[]
        for (title,ntags,rp) in notes:
            rel=str(rp.relative_to(CONTENT))
            if any(f in rel for f in folders) or any(t in ntags for t in tags):
                chosen.append(title)
        chosen=sorted(set(chosen), key=str.lower)
        listmd = "## Contents\n\n" + ("\n".join(f"- [[{t}]]" for t in chosen) if chosen else "_No notes yet._") + \
                 f"\n\n<small>{len(chosen)} notes · live filterable table available in Obsidian (Dataview).</small>\n"
        # remove the dataview block and the info callout that followed it
        txt=re.sub(r"```dataview\s*.*?```", listmd, txt, count=1, flags=re.S)
        txt=re.sub(r"^> \[!info\].*?Community plugins\.\s*$", "", txt, flags=re.M|re.S)
        p.write_text(txt, encoding="utf-8")

if __name__=="__main__":
    mirror()
    flatten_multicolumn()
    downscale_images()
    de_dataview(index_notes())
    print("published: content/ mirrored from vault; images downscaled; Map dataview blocks -> static link lists")
