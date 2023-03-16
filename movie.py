import json
import os
import logging

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

    @classmethod
    def add_to_movies(cls, title):
        movies = cls._get_movies()
        if title.title() not in movies:
            movies.append(title.title())
            cls._write_movies(movies)
            logging.info(f"{title} a été ajouté dans la liste des films.")
        else:
            logging.info(f"{title} est déjà dans la liste de films.")

if __name__ == "__main__":
    m = Movie("Le seigneur des anneaux")
    # print(m._write_movies(["Alice in wonderland", "Mary Poppins"]))
    # print(m)
    # m.add_to_movies()