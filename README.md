# cine-club-api
# Documentation for the Python GUI Cinema API

This GUI was created using Python with the PySide2 library for the user interface and the built-in `json` module for JSON file management. The interface allows the user to enter movie titles, save them to an external JSON file, display them, and delete them while updating the JSON file.

## Installation and Usage

To use this GUI, follow these steps:

1. Clone the GitHub repository containing the code for the GUI to your local machine.
2. Install the necessary dependencies. You can install them using the following command:

    ```
    pip install PySide2
    ```

3. Run the `main.py` file using the following command:

    ```
    python main.py
    ```

## Using the GUI

### Adding a movie

The user can add a new movie by entering the movie title in the text field and clicking the "Add" button. The movie title will be added to the list of movies on the screen and will also be saved in the external JSON file.

### Displaying movies

The user can display the list of movies by clicking the "Show movies" button. This will display the list of movies in the console and in a dialog box on the screen.

### Deleting a movie

The user can delete a movie by selecting the movie title from the list of movies and clicking the "Delete" button. The movie title will be removed from the list of movies on the screen and will also be removed from the external JSON file.

## Managing the external JSON file

The external JSON file is used to store the movie titles added by the user. The file is located in a `data` folder in the same directory as `main.py` and is named `movies.json`. The movie titles are stored as a JSON list.

When a new movie is added or a movie is deleted, the external JSON file is automatically updated.
