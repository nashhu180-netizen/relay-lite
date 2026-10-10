"""Same Unicode-character basis for tracked skill Markdown/TOML, baseline vs checkout."""
from pathlib import Path
import json,subprocess
root=Path(__file__).resolve().parents[6]
base='9f7c2b2c15dca69ce39a780aa4b7c4bc64ea6c70'
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',base,'--','skill'],cwd=root,text=True).splitlines()
paths=[p for p in paths if Path(p).suffix in ('.md','.toml')]
rows=[]
for path in paths:
 before=len(subprocess.check_output(['git','show',base+':'+path],cwd=root).decode())
 after=len((root/path).read_text(encoding='utf-8'))
 rows.append(dict(path=path,before=before,after=after,delta=after-before))
print(json.dumps({'baseline':base,'basis':'Unicode code points including whitespace in skill md/toml','before':sum(r['before'] for r in rows),'after':sum(r['after'] for r in rows),'files':rows},ensure_ascii=False,indent=2))
