# movie.py

from database import get_connection

def add_movie():
    title = input("Enter movie title: ")
    duration = input("Enter movie duration in minutes: ")
    genre = input("Enter movie genre: ")

    try:
        duration = int(duration)
    except ValueError:
        print("Invalid duration. Setting to 0.")
        duration = 0

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO movies (title, duration, genre) VALUES (?, ?, ?)',
                       (title, duration, genre))
        conn.commit()
        print(f"Movie '{title}' added successfully.")

def list_movies():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()

        if not movies:
            print("No movies available.")
            return

        print("\n--- Movies List ---")
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Duration: {movie[2]} min, Genre: {movie[3]}")

def remove_movie():
    list_movies()
    movie_id = input("Enter Movie ID to remove: ")
    try:
        movie_id = int(movie_id)
    except ValueError:
        print("Invalid ID.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
        conn.commit()
        print(f"Movie ID {movie_id} removed.")
