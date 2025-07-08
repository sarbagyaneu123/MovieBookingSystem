# booking.py

from database import get_connection  # Import the function to connect to the SQLite database

def add_booking():
    # Start a database connection
    with get_connection() as conn:
        cursor = conn.cursor()

        # Fetch all showtimes with movie details
        cursor.execute('''
            SELECT showtimes.id, movies.title, movies.genre, showtimes.time, showtimes.seat_capacity, showtimes.seats_booked
            FROM showtimes
            JOIN movies ON showtimes.movie_id = movies.id
        ''')
        showtimes = cursor.fetchall()

        # If there are no showtimes, inform the user
        if not showtimes:
            print("No showtimes available.")
            return

        # Display available showtimes with remaining seats
        print("Available Showtimes:")
        for showtime in showtimes:
            available = showtime[4] - showtime[5]  # seat_capacity - seats_booked
            print(f"{showtime[0]}: {showtime[1]} ({showtime[2]}) at {showtime[3]} - Available: {available}/{showtime[4]}")

        # Ask user to select a showtime and input booking details
        showtime_id = input("Enter Showtime ID to book: ")
        user_name = input("Enter your name: ")
        seats = input("Enter number of seats: ")

        # Validate input values
        try:
            showtime_id = int(showtime_id)
            seats = int(seats)
            if seats <= 0:
                print("Seats must be positive.")
                return
        except ValueError:
            print("Invalid input.")
            return

        # Check if enough seats are available for the selected showtime
        cursor.execute('SELECT seat_capacity, seats_booked FROM showtimes WHERE id = ?', (showtime_id,))
        row = cursor.fetchone()
        if not row:
            print("Showtime not found.")
            return

        seat_capacity, seats_booked = row
        available = seat_capacity - seats_booked

        if seats > available:
            print(f"Error: Only {available} seats available.")
            return

        # All good, proceed to insert the booking into the bookings table
        cursor.execute('INSERT INTO bookings (showtime_id, user_name, seats) VALUES (?, ?, ?)',
                       (showtime_id, user_name, seats))

        # Update the showtime's booked seat count
        cursor.execute('UPDATE showtimes SET seats_booked = seats_booked + ? WHERE id = ?',
                       (seats, showtime_id))

        # Save changes
        conn.commit()

        print(f"Booking confirmed for {user_name} for {seats} seats.")

def list_bookings():
    # Start a new database connection to read bookings
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Get all bookings joined with movie and showtime information
        cursor.execute('''
            SELECT bookings.id, bookings.user_name, movies.title, movies.genre, showtimes.time, bookings.seats
            FROM bookings
            JOIN showtimes ON bookings.showtime_id = showtimes.id
            JOIN movies ON showtimes.movie_id = movies.id
        ''')
        bookings = cursor.fetchall()

        # Show message if there are no bookings yet
        if not bookings:
            print("No bookings found.")
            return

        # Nicely format and display each booking
        print("\n--- Bookings List ---")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, User: {booking[1]}, Movie: {booking[2]} ({booking[3]}), Time: {booking[4]}, Seats: {booking[5]}")

def remove_booking():
    # Show all current bookings so the user can pick one to cancel
    list_bookings()
    booking_id = input("Enter Booking ID to cancel: ")

    try:
        booking_id = int(booking_id)
    except ValueError:
        print("Invalid ID.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()

        # First, get the booking details to release the booked seats
        cursor.execute('SELECT showtime_id, seats FROM bookings WHERE id = ?', (booking_id,))
        row = cursor.fetchone()

        # If the booking exists, update the showtime's seat count
        if row:
            showtime_id, seats = row
            cursor.execute('UPDATE showtimes SET seats_booked = seats_booked - ? WHERE id = ?', (seats, showtime_id))

        # Delete the booking entry from the table
        cursor.execute('DELETE FROM bookings WHERE id = ?', (booking_id,))
        conn.commit()

        print(f"Booking ID {booking_id} canceled.")
