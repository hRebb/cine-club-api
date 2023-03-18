from PySide2 import QtWidgets
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle("Py Cinema Club")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.add_button = QtWidgets.QPushButton("Add")
        self.list_widget = QtWidgets.QListWidget(self)
        self.rm_button = QtWidgets.QPushButton("Remove")

        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.rm_button)

    def setup_connections(self):
        self.add_button.clicked.connect(self.add_movie)
        self.lineEdit.returnPressed.connect(self.add_movie)
        self.rm_button.clicked.connect(self.remove_movie)

    def populate_movies(self):
        self.movies = get_movies()
        for movie in self.movies:
            self.list_widget.addItem(movie.title)

    def add_movie(self):
        movie_title = self.lineEdit.text().strip()

        if not movie_title:
            return False
        
        movie = Movie(movie_title)
        result = movie.add_to_movies()

        if not result:
            return False
        else:
            self.list_widget.addItem(movie.title)
            self.lineEdit.clear()

    def remove_movie(self):
        print("Removing movies")

app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()