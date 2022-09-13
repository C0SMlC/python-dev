from pathlib import Path

path = Path("Formatting")
# print(path.exists())
# print(path.mkdir())  # --->>> MAKE DIRECTORY
# print(path.rmdir())  # --->>> MAKE DIRECTORY
# print(path.rmdir())
# print(path.rename("Ecommerce2"))
print(path.iterdir())  # --->>> Iterate

for p in path.iterdir():
    print(p)
