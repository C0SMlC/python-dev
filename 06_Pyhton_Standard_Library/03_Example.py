from pathlib import Path

path = Path("05_Modules/Add/01_ImportingModules.py")
print(path.exists())
print(path.is_file())
print(path.name)
print(path.suffix)
print(path.stem)
print(path.parent)
print(path.with_suffix(".txt"))
print(path.with_name("File.txt"))
