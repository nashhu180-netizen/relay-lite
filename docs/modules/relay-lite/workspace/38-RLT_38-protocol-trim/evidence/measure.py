"""Reproduce RLT_38 character accounting; run at repository root."""
import json
from pathlib import Path
import subprocess
BASE='0b08c18be09cd00e84ff214c582941593ca7c2ec'
old={p:subprocess.check_output(['git','show',BASE+':'+p]).decode('utf-8') for p in subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'--','skill']).decode().splitlines() if p.endswith(('.md','.toml'))}
new={p.as_posix():p.read_bytes().decode('utf-8') for p in Path('skill').rglob('*') if p.is_file() and p.suffix in ('.md','.toml')}
rows=[{'path':p,'before':len(old.get(p,'')),'after':len(new.get(p,'')),'delta':len(new.get(p,''))-len(old.get(p,''))} for p in sorted(old.keys()|new.keys())]
a=sum(map(len,old.values()));b=sum(map(len,new.values()))
print(json.dumps({'baseline_sha':BASE,'unit':'Unicode code points after UTF-8 decoding; includes whitespace and line breaks; skill md/toml only; excludes helper Python scripts in installed package','before':a,'after':b,'reduction':a-b,'reduction_percent':round((a-b)*100/a,2),'files':rows,'accounting':'New references are included in after total. Relocation alone contributes zero savings; totals include new routing and contract compression. Per-character semantic attribution is not claimed; rule-map and section-map show conservation.'},ensure_ascii=False,indent=2))
