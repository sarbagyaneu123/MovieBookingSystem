# 🎟️ Movie Ticket Booking System

A simple Python-based movie ticket booking system using SQLite. It allows users to view available movies and showtimes, book tickets, and manage bookings via a command-line interface. The system simulates a real-world movie theater booking experience with an interactive menu.

---

## 💻 How to Run

1. **Clone the repository:**
git clone https://github.com/sarbagyaneu123/MovieBookingSystem
2. Navigate into the project folder:
cd MovieBookingSystem
3. Run the application:
python main.py

🐍 Python Requirements
Python Version: 3.10+

Libraries Used:

sqlite3 (built-in)

📌 Note: This project uses only Python's standard library. No need to install external packages.

📂 Project Structure
plaintext
Copy
Edit
MovieBookingSystem/
├── main.py               # Entry point of the application
├── booking_system.py     # Handles booking logic
├── database.py           # Manages SQLite DB operations
├── utils.py              # Utility functions (e.g., validation)
├── movie.db              # SQLite database file
└── README.md             # Project documentation

📌 Features
View available movies and showtimes

Book tickets by entering movie ID, seat number, and name

View all bookings stored in the database

Cancel a booking

Prevents duplicate seat bookings

Clean and readable CLI interface

🛠️ Future Improvements
Add GUI with Tkinter or PyQt

Include admin panel for movie management

Add user login system

📄 License
This project is open-source and free to use.

👨‍💻 Author
Developed by Sarbagya Neupane
