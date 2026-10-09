"""Simple repository hygiene checker for demonstration CI; not a full secret scanner."""
from pathlib import Path
import re,sys,json
PATTERNS=[
 ("private-key-marker",re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
 ("credential-assignment",re.compile(r"""(?i)\b(?:api_key|access_token|client_secret)\s*[:=]\s*['"][^'"]{12,}['"]""")),
]
SKIP={".git",".venv","venv","node_modules","__pycache__"}
def scan(root):
 base=Path(root)
 if not base.is_dir(): raise ValueError("Root must be a directory")
 findings=[]
 for path in base.rglob("*"):
  if not path.is_file() or any(part in SKIP for part in path.parts): continue
  try:
   if path.stat().st_size>1_000_000: continue
   lines=path.read_text(encoding="utf-8").splitlines()
  except (UnicodeDecodeError,OSError): continue
  for number,line in enumerate(lines,1):
   for rule,pattern in PATTERNS:
    if pattern.search(line): findings.append({"file":str(path.relative_to(base)),"line":number,"rule":rule})
 return findings
if __name__=="__main__":
 results=scan(sys.argv[1] if len(sys.argv)>1 else ".")
 print(json.dumps(results,indent=2))
 raise SystemExit(1 if results else 0)
