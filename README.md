# Movie Filter Application

---

## Description
The Movie Filter Application is a Python program designed to load movie data from a CSV file and allow users to filter and view movies based on different criteria such as name, year, and director. Users can interact with the program through a simple text-based menu interface.

## Features
1. **Filter Movies By Name:** Allows users to view a list of all movies sorted by their names.
2. **Filter Movies By Year:** Displays a list of all movies sorted by their release years.
3. **Filter Movies By Director:** Shows a list of all movies sorted by their directors.
4. **See All Movies:** Displays all movie data available in the CSV file.
5. **Exit:** Terminates the program.

## Files
- **Movie_Filtering_System.py:** The main Python script containing the Movie Filter Application code.
- **Movies.csv:** The CSV file containing movie data. The format should be `[Name, Year, Director]`.
- **Dockerfile:** Docker configuration to containerize and run the application easily.

## Usage (Local)
1. Ensure Python 3.x is installed on your system.
2. Ensure the `Movies.csv` file is in the same directory as the `Movie_Filtering_System.py` script.
3. Run the script:
   ```sh
   python Movie_Filtering_System.py
   ```
4. Follow the on-screen prompts to navigate through the menu options.
5. To exit the program, choose the "Exit" option from the menu.

## Usage (Docker)
1. Make sure Docker is installed and running on your system.
2. Build the Docker image:
   ```sh
   docker build -t movie-filter-app .
   ```
3. Run the application in a container:
   ```sh
   docker run -it movie-filter-app
   ```

## Dependencies
- Python 3.x (standard library only)
- Docker (for containerized usage)

## Sample CSV File Format (`Movies.csv`)
```csv
Name,Year,Director
The Shawshank Redemption,1994,Frank Darabont
The Godfather,1972,Francis Ford Coppola
Inception,2010,Christopher Nolan
```
