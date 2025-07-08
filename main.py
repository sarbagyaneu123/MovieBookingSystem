# main.py

import movie
import showtime
import booking
from database import initialize_database

def admin_menu():
    while True:
        print("""
--- Admin Menu ---
1. Add Movie
2. List Movies
3. Remove Movie
4. Add Showtime
5. List Showtimes
6. Remove Showtime
7. List Bookings
8. Remove Booking
0. Logout
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            movie.add_movie()
        elif choice == "2":
            movie.list_movies()
        elif choice == "3":
            movie.remove_movie()
        elif choice == "4":
            showtime.add_showtime()
        elif choice == "5":
            showtime.list_showtimes()
        elif choice == "6":
            showtime.remove_showtime()
        elif choice == "7":
            booking.list_bookings()
        elif choice == "8":
            booking.remove_booking()
        elif choice == "0":
            break

def user_menu():
    while True:
        print("""
--- User Menu ---
1. List Movies
2. List Showtimes
3. Add Booking
4. List Bookings
0. Logout
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            movie.list_movies()
        elif choice == "2":
            showtime.list_showtimes()
        elif choice == "3":
            booking.add_booking()
        elif choice == "4":
            booking.list_bookings()
        elif choice == "0":
            break

def main():
    initialize_database()
    while True:
        print("""
--- Cinema Booking System ---
1. Admin Login
2. User Access
0. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            admin_menu()
        elif choice == "2":
            user_menu()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
