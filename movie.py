class Movie:
    def __init__(self, title) -> str:
        self.title = title.title()

    def __str__(self) -> str:
        return f"{self.title}"
    

if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)