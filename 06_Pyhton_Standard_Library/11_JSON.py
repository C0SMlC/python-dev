# JAVASCRIPT OBJECT NOTATION

import json
from pathlib import Path

movies = [
    {"id": 1, "Title": "Avengers Endgame", "Year": 2018},
    {"id": 2, "Title": "Spiderman No Way Home", "Year": 2021}
]

data = json.dumps(movies)
Path("Movies.json").write_text(data)
