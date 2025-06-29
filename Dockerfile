#Official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

#Python script and CSV file
COPY Movie_Filtering_System.py ./
COPY Movies.csv ./

#default command to run the app
CMD ["python", "Movie_Filtering_System.py"]
