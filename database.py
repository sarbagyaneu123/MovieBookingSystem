import sqlite3

DB_FILE = 'cinema.db'  # Name of the SQLite database file

def get_connection():
    # Function to create and return a connection to the database
    return sqlite3.connect(DB_FILE)

def initialize_database():
    # Set up the database tables if they don't already exist
    with get_connection() as conn:
        cursor = conn.cursor()

        # Create the 'movies' table to store movie details
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration INTEGER,        -- Duration of the movie in minutes
                genre TEXT              -- Genre of the movie (e.g., Action, Drama)
            )
        ''')

        # Create the 'showtimes' table to store when movies are shown
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS showtimes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,          -- Link to the movie
                time TEXT,                 -- Showtime (e.g., "2025-07-08 19:30")
                seat_capacity INTEGER,     -- Total seats available for the show
                seats_booked INTEGER DEFAULT 0,  -- Seats already booked
                FOREIGN KEY(movie_id) REFERENCES movies(id)  -- Enforce movie_id validity
            )
        ''')

        # Create the 'bookings' table to record user reservations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                showtime_id INTEGER,       -- Link to the showtime
                user_name TEXT,            -- Name of the person booking
                seats INTEGER,             -- Number of seats booked
                FOREIGN KEY(showtime_id) REFERENCES showtimes(id)  -- Enforce showtime_id validity
            )
        ''')

        # Save changes to the database
        conn.commit()
        print("Database initialized successfully.")
