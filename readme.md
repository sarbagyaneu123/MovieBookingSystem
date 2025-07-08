# 🎬 MovieBookingSystem

A terminal-based movie ticket booking system built with **Python** and **SQLite**. This project allows users to manage movies, showtimes, and bookings through a simple command-line interface. It demonstrates SQLite-based data persistence, modular Python design, and CRUD operations in a real-world scenario.

---

## 🚀 Features

- 👤 Admin & User Modes  
- 🎞️ Add, List, and Remove Movies  
- 🕒 Manage Showtimes for Movies  
- 🎟️ Book Seats and Manage Bookings  
- 🗃️ SQLite Database Backend (`cinema.db`)  
- 🧩 Modular Code for Better Maintainability  

---

## 📁 Project Structure

MovieBookingSystem/
├── main.py # Application entry point and menu system
├── database.py # SQLite DB connection and table initialization
├── movie.py # Movie CRUD operations
├── showtime.py # Showtime CRUD operations
├── booking.py # Booking logic
├── cinema.db # SQLite DB file (auto-created)
└── README.md # Project documentation


## 💻 How to Run

1. **Clone the repository:**


git clone https://github.com/sarbagyaneu123/MovieBookingSystem.git
cd MovieBookingSystem
Run the program:

bash
Copy
Edit
python main.py
💡 The database (cinema.db) will be created automatically on the first run.

📝 Usage Overview
Admin Menu:

Add/List/Remove Movies

Add/List/Remove Showtimes

View and Cancel Bookings

User Menu:

View Movies and Showtimes

Book Tickets

View Your Bookings

Booking Flow:

Select movie and showtime

Enter your name and number of seats

Booking is confirmed if seats are available

👨‍💻 Code Highlights
database.py: Initializes SQLite DB and required tables

movie.py: Handles movie-related CRUD operations

showtime.py: Manages showtimes linked to movies

booking.py: Handles seat booking and cancellation logic

main.py: CLI-based interface for both Admin and User

🎯 Purpose
This project was developed as part of the Analyst Trainee Assessment. It demonstrates proficiency in:

Database integration

Command-line interface development

Modular and scalable code design

Real-world application of CRUD logic

📫 Author
Sarbagya Neupane
🔗 https://github.com/sarbagyaneu123 

