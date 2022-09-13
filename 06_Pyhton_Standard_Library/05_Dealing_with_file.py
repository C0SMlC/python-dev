from pathlib import Path
from time import ctime

path = Path("Extra\ecommerce.py")
#  print(path.stat())
print(ctime(path.stat().st_mtime))
print(path.read_text())
print(path.read_bytes())
path.write_text("print(\"LOL\")")
print(path.read_text())
