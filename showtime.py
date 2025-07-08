from database import get_connection  # Import function to connect to the database

def add_showtime():
    # Add a new showtime for an existing movie
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Fetch all movies to let the user select which movie to add showtime for
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()

        if not movies:
            print("No movies available. Add movies first.")  # No movies yet, so can't add showtimes
            return

        # Display available movies for user selection
        print("Available Movies:")
        for movie in movies:
            print(f"{movie[0]}: {movie[1]} ({movie[2]} min, {movie[3]})")

        # Get user input for movie ID, showtime, and seat capacity
        movie_id = input("Enter Movie ID for showtime: ")
        time = input("Enter showtime (e.g. 15:30): ")
        seat_capacity = input("Enter seat capacity: ")

        # Validate inputs
        try:
            movie_id = int(movie_id)
            seat_capacity = int(seat_capacity)
            if seat_capacity <= 0:
                print("Seat capacity must be positive.")
                return
        except ValueError:
            print("Invalid input.")
            return

        # Insert the new showtime into the database
        cursor.execute('INSERT INTO showtimes (movie_id, time, seat_capacity) VALUES (?, ?, ?)',
                       (movie_id, time, seat_capacity))
        conn.commit()
        print(f"Showtime added successfully.")

def list_showtimes():
    # Display all showtimes along with movie details and seat availability
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT showtimes.id, movies.title, movies.genre, showtimes.time, showtimes.seat_capacity, showtimes.seats_booked
            FROM showtimes
            JOIN movies ON showtimes.movie_id = movies.id
        ''')
        showtimes = cursor.fetchall()

        if not showtimes:
            print("No showtimes available.")
            return

        print("\n--- Showtimes List ---")
        for showtime in showtimes:
            # Calculate available seats by subtracting booked seats from total capacity
            available_seats = showtime[4] - showtime[5]
            print(f"ID: {showtime[0]}, Movie: {showtime[1]} ({showtime[2]}), Time: {showtime[3]}, Seats Available: {available_seats}/{showtime[4]}")

def remove_showtime():
    # Remove a showtime by ID after listing all showtimes
    list_showtimes()
    showtime_id = input("Enter Showtime ID to remove: ")
    try:
        showtime_id = int(showtime_id)
    except ValueError:
        print("Invalid ID.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM showtimes WHERE id = ?', (showtime_id,))
        conn.commit()
        print(f"Showtime ID {showtime_id} removed.")
