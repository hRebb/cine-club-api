from PySide2 import QtWidgets, QtCore
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
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
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
        
        self.lineEdit.setText("")

    def remove_movie(self):
        selected_items = self.list_widget.selectedItems()

        for item in selected_items:
            movie_title = item.text()
            movie = Movie(movie_title)

            result = movie.remove_from_movies()

            if result:
                self.list_widget.takeItem(self.list_widget.row(item))

app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()