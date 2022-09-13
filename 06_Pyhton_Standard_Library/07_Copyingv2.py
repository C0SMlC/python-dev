from pathlib import Path
from time import ctime
import shutil  # for copying file
source = Path("Extra\ecommerce.py")
target = Path("Extra1") / "ecommerce.py"
shutil.copy(source, target)
