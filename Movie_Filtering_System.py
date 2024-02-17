import os
import time
import csv

def load_movies_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        movies_data = [row for row in reader]
    return movies_data

def prettyPrint():
    os.system("cls" if os.name == "nt" else "clear")
    print("Best All Time Movies")
    print()

def filter_movies_by_name(movies_data):
    prettyPrint()
    print("Movies By Name")
    print("--------------------------------------------")
    for movie in movies_data[1:]:
        print(movie[0])
    print("--------------------------------------------")
    input("Press Enter to continue...")

def filter_movies_by_year(movies_data):
  prettyPrint()
  print("Movies By Year")
  print("--------------------------------------------")
  for movie in movies_data[1:]:
    print(movie[1])
  print("--------------------------------------------")
  input("Press Enter to continue...")

def filter_movies_by_director(movies_data):
  prettyPrint()
  print("Movies By Director")
  print("--------------------------------------------")
  for movie in movies_data[1:]:
    print(movie[2])
  print("--------------------------------------------")
  input("Press Enter to continue...")

def see_all(movies_data):
  prettyPrint()
  print("Movies By Director")
  print("--------------------------------------------")
  for movie in movies_data[1:]:
    print(movie)
  print("--------------------------------------------")
  input("Press Enter to continue...")


def main():
    file_path = "/Users/elierestopinan/Documents/3- 🏷️ Resources/python_projects/Movie_Filter/Movies.csv"
    if not os.path.isfile(file_path):
        print("Error: File 'Movies.csv' not found in 'Movies File' folder.")
        return

    movies_data = load_movies_from_csv(file_path)

    while True:
        prettyPrint()
        print("--------------------------------------------")
        print("Please Select one of the following options:")
        print()
        menu = input("1. Filter Movies By Name.\n2. Filter Movies by Year\n3. Filter Movies by Director\n4. See all Movies\n5. Exit\n> ")

        if menu == "1":
            filter_movies_by_name(movies_data)
        if menu == "2":
            filter_movies_by_year(movies_data)
        if menu == "3":
          filter_movies_by_director(movies_data)
        if menu == "4":
          see_all(movies_data)
        elif menu == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
print ()
