from pathlib import Path

source = Path("Extra\ecommerce.py")
target = Path("Extra1") / "ecommerce.py"

target.write_text(source.read_text())
