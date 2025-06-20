# Expense_Tracker_App
# 💸 Expense Tracker App using Django

A simple and user-friendly **Expense Tracker** web application built with **Django**. This app helps users manage their daily expenses efficiently by adding, editing, and categorizing transactions.

## 📌 Features

- ✅ Add, edit, and delete expenses
- 📅 Filter expenses by date
- 💼 Categorize expenses (e.g., Food, Transport, Bills)
- 📊 View total expense summary
- 🔒 User authentication (Login, Logout, Register)
- 💡 Clean and responsive UI

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default with Django)

## 📂 Project Structure

<pre>
Expense_Tracker_App_using_Django/
├── mysite/
│   ├── expenseapp/
│   ├── mysite/
│   ├── db.sqlite3
│   └── manage.py
</pre>

### Screenshot 1: Add,Update and delete expense & give total expense amount

<p align="center">
  <img src="images/screenshot1.png"  width="600" />
</p>

### Screenshot 2: Filter expenses by date and categorize expense
<p align="center">
  <img src="images/screenshot2.png"  width="600" />
</p>

### Screenshot 3: Expense spread across categories using pie chart and daily expense sum using line chart 
<p align="center">
  <img src="images/screenshot3.png"  width="600" />
</p>



## 🚀 Getting Started

Follow these steps to run the project locally.

```bash
1. clone the Repository
   git clone https://github.com/rashi311/Expense_Tracker_App_using_Django.git
   cd Expense_Tracker_App_using_Django/mysite


2. Create and Activate Virtual Environment
   python -m venv env
   source env/bin/activate

3. Install Required Packages
   pip install -r ../requirements.txt

4. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create Superuser (for admin acces)
   python manage.py createsuperuser

6. Run the Server
   Python manage.py runserver

🧪 Testing
   You can run tests using:
   python manage.py test

