from database import get_connection  # Import the database connection function

def add_movie():
    # Ask user for movie details
    title = input("Enter movie title: ")
    duration = input("Enter movie duration in minutes: ")
    genre = input("Enter movie genre: ")

    # Convert duration input to integer, default to 0 if invalid
    try:
        duration = int(duration)
    except ValueError:
        print("Invalid duration. Setting to 0.")
        duration = 0

    # Insert the new movie into the movies table
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO movies (title, duration, genre) VALUES (?, ?, ?)',
                       (title, duration, genre))
        conn.commit()
        print(f"Movie '{title}' added successfully.")

def list_movies():
    # Retrieve and display all movies from the database
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()

        # Inform the user if no movies are found
        if not movies:
            print("No movies available.")
            return

        # Print a nicely formatted list of movies
        print("\n--- Movies List ---")
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Duration: {movie[2]} min, Genre: {movie[3]}")

def remove_movie():
    # Show all movies so the user can choose which one to remove
    list_movies()
    movie_id = input("Enter Movie ID to remove: ")

    # Validate input
    try:
        movie_id = int(movie_id)
    except ValueError:
        print("Invalid ID.")
        return

    # Delete the selected movie from the database
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movies WHERE id = ?', (movie_id,))
        conn.commit()
        print(f"Movie ID {movie_id} removed.")
