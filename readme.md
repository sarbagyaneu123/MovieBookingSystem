# 🎬 MovieBookingSystem

A terminal-based movie ticket booking system built with Python and SQLite. This project enables users to manage movies, showtimes, and bookings through a simple command-line interface. It demonstrates use of SQLite for data persistence, modular Python programming, and practical CRUD operations.

---

## 🚀 Features

- 👤 Admin & User modes  
- 🎞️ Add, list, and remove movies  
- 🕒 Add, list, and remove showtimes for movies  
- 🎟️ Book seats for showtimes and manage bookings  
- 🗃️ SQLite database backend (`cinema.db`) for persistent storage  
- 🧩 Modular code structure for maintainability

---

## 📁 Project Structure

MovieBookingSystem/
├── main.py # Application entry point and menus
├── database.py # SQLite database connection and initialization
├── movie.py # Movie management (CRUD)
├── showtime.py # Showtime management (CRUD)
├── booking.py # Booking management
├── cinema.db # SQLite database file (created on init)
└── README.md # Project documentation
---

## 💻 How to Run

1. Clone the repository:

```bash
git clone https://github.com/sarbagyaneu123/MovieBookingSystem.git
cd MovieBookingSystem
Run the program:

bash
Copy
Edit
python main.py
The program will initialize the database on first run and create necessary tables if missing.

📝 Usage Overview
Admin Menu: Manage movies, showtimes, bookings, and perform removals.

User Menu: View movies, showtimes, make bookings, and view your bookings.

Booking Flow: Choose a showtime from available options, enter your name and number of seats, booking is confirmed if seats are available.

Data Persistence: All data is stored in the cinema.db SQLite database file.

👨‍💻 Code Highlights
database.py handles DB connection and creates tables if they don't exist.

movie.py manages adding, listing, and removing movies.

showtime.py manages showtimes linked to movies.

booking.py lets users book seats, list bookings, and cancel bookings.

main.py provides a CLI menu for admin and user interactions.

🎯 Purpose
This project was developed as part of an assessment for the Analyst Trainee role. It demonstrates database integration, user input validation, and clean modular coding practices.

📫 Author
Sarbagya Neupane
GitHub: "https://github.com/sarbagyaneu123"