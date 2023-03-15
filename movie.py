import json
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

class Movie:
    def __init__(self, title) -> str:
        self.title = title.title()

    def __str__(self) -> str:
        return f"{self.title}"
    
    @staticmethod
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def _write_movies(movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)

if __name__ == "__main__":
    m = Movie("Le seigneur des anneaux")
    print(m._write_movies(["Alice in wonderland", "Mary Poppins"]))
    #print(m)