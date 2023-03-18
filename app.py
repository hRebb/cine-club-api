from PySide2 import QtWidgets
from movie import get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.setup_ui()
        self.populate_movies()

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

    def populate_movies(self):
        self.movies = get_movies()
        for movie in self.movies:
            self.list_widget.addItem(movie.title)

app = QtWidgets.QApplication([])

win = App()
win.show()

app.exec_()