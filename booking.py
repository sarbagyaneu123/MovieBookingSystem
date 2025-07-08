# booking.py

from database import get_connection

def add_booking():
    with get_connection() as conn:
        cursor = conn.cursor()

        # List showtimes with available seats
        cursor.execute('''
            SELECT showtimes.id, movies.title, movies.genre, showtimes.time, showtimes.seat_capacity, showtimes.seats_booked
            FROM showtimes
            JOIN movies ON showtimes.movie_id = movies.id
        ''')
        showtimes = cursor.fetchall()

        if not showtimes:
            print("No showtimes available.")
            return

        print("Available Showtimes:")
        for showtime in showtimes:
            available = showtime[4] - showtime[5]
            print(f"{showtime[0]}: {showtime[1]} ({showtime[2]}) at {showtime[3]} - Available: {available}/{showtime[4]}")

        showtime_id = input("Enter Showtime ID to book: ")
        user_name = input("Enter your name: ")
        seats = input("Enter number of seats: ")

        try:
            showtime_id = int(showtime_id)
            seats = int(seats)
            if seats <= 0:
                print("Seats must be positive.")
                return
        except ValueError:
            print("Invalid input.")
            return

        # Check availability
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

        # Add booking and update showtime
        cursor.execute('INSERT INTO bookings (showtime_id, user_name, seats) VALUES (?, ?, ?)',
                       (showtime_id, user_name, seats))
        cursor.execute('UPDATE showtimes SET seats_booked = seats_booked + ? WHERE id = ?',
                       (seats, showtime_id))
        conn.commit()

        print(f"Booking confirmed for {user_name} for {seats} seats.")

def list_bookings():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT bookings.id, bookings.user_name, movies.title, movies.genre, showtimes.time, bookings.seats
            FROM bookings
            JOIN showtimes ON bookings.showtime_id = showtimes.id
            JOIN movies ON showtimes.movie_id = movies.id
        ''')
        bookings = cursor.fetchall()

        if not bookings:
            print("No bookings found.")
            return

        print("\n--- Bookings List ---")
        for booking in bookings:
            print(f"Booking ID: {booking[0]}, User: {booking[1]}, Movie: {booking[2]} ({booking[3]}), Time: {booking[4]}, Seats: {booking[5]}")

def remove_booking():
    list_bookings()
    booking_id = input("Enter Booking ID to cancel: ")
    try:
        booking_id = int(booking_id)
    except ValueError:
        print("Invalid ID.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()

        # Release seats
        cursor.execute('SELECT showtime_id, seats FROM bookings WHERE id = ?', (booking_id,))
        row = cursor.fetchone()
        if row:
            showtime_id, seats = row
            cursor.execute('UPDATE showtimes SET seats_booked = seats_booked - ? WHERE id = ?', (seats, showtime_id))

        # Delete booking
        cursor.execute('DELETE FROM bookings WHERE id = ?', (booking_id,))
        conn.commit()
        print(f"Booking ID {booking_id} canceled.")
