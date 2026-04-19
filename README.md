# 💰 Expense Tracker Web App

#### Video Demo: https://youtu.be/OPXC9oSCr4M

## 📌 Description

This project is a full-stack Expense Tracker Web Application developed as my final project for CS50x. The purpose of this application is to help users manage their daily expenses in an organized and user-friendly way.

The application allows users to register and log in securely using a session-based authentication system. Once logged in, users can add, view, edit, and delete their expenses. Each expense includes an amount, category, description, and date.

The dashboard provides a summary of all expenses, including the total amount spent and a category-wise breakdown. A bar chart is used to visually represent spending patterns, making it easier for users to understand their financial habits.

This project is built using Flask for the backend, SQLite for the database, and HTML, CSS, and JavaScript for the frontend. Jinja2 templates are used to dynamically render data from the backend.

---

## 🚀 Features

- User Registration and Login
- Session-based Authentication
- Add, Edit, and Delete Expenses
- Dashboard with total expense summary
- Category-wise tracking
- Chart visualization (Chart.js)
- Responsive UI with modern styling
- Dark mode toggle

---

## 🛠️ Tech Stack

- Python (Flask)
- SQLite
- HTML, CSS
- JavaScript
- Jinja2
- Chart.js

---

## 📁 Project Structure
expense_project/
├── app.py
├── database.db
├── requirements.txt
├── README.md
├── templates/
│ ├── layout.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── add.html
│ ├── edit.html
├── static/
│ └── style.css


## ⚙️ How It Works

Users first register and log in to access the application. After authentication, each user can manage their own expenses. Data is stored in an SQLite database and linked to the logged-in user.

The dashboard calculates the total expense and groups data by category. This data is passed to the frontend and displayed using a chart for better visualization.

Users can update or remove expenses at any time, giving them full control over their records.

---

## 🧠 Design Decisions

- **Flask** was used for its simplicity and flexibility.
- **SQLite** was chosen for easy setup and lightweight storage.
- **Session-based authentication** was implemented to keep login handling simple.
- **Chart.js** was used for clean and interactive charts.
- The UI was designed to be simple, responsive, and user-friendly.

---

## 🔮 Future Improvements

- Add password hashing for better security
- Export data (CSV/PDF)
- Add filters and search
- Monthly reports
- Convert frontend to React

---

## 🎯 Conclusion

This project demonstrates my ability to build a complete web application using backend, database, and frontend technologies. It reflects the concepts learned in CS50, including authentication, database management, and dynamic web development.
