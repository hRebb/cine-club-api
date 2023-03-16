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


    def add_to_movies(self):
        movies = self._get_movies(self)
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} est déjà dans la liste de films.")
            return False
        
    def remove_from_movies(self):
        movies = self._get_movies(self)
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            print(logging.info(f"{self.title} a été retiré de la liste de films."))
            return True
        else:
            logging.warning(f"{self.title} n'est pas dans la liste de films")
            return False

if __name__ == "__main__":
    m = Movie("Harry Potter")
    m.remove_from_movies()