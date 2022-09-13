from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("Extra/ecommerce.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("Extract")
