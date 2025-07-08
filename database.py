# database.py

import sqlite3

DB_FILE = 'cinema.db'

def get_connection():
    return sqlite3.connect(DB_FILE)

def initialize_database():
    with get_connection() as conn:
        cursor = conn.cursor()

        # Create Movies table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration INTEGER,
                genre TEXT
            )
        ''')

        # Create Showtimes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS showtimes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                time TEXT,
                seat_capacity INTEGER,
                seats_booked INTEGER DEFAULT 0,
                FOREIGN KEY(movie_id) REFERENCES movies(id)
            )
        ''')

        # Create Bookings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                showtime_id INTEGER,
                user_name TEXT,
                seats INTEGER,
                FOREIGN KEY(showtime_id) REFERENCES showtimes(id)
            )
        ''')

        conn.commit()
        print("Database initialized successfully.")
