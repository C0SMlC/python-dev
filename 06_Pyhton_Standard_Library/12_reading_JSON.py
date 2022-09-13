import json
from pathlib import Path

data = Path("Extract\Movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[1]["Title"])
