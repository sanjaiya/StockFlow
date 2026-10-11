# StockFlow – Quality & Inventory Management System

## About
StockFlow is a web-based inventory management system built using Python and Django. It helps manage products, suppliers, and stock records.

## Features
- Add, view, edit, and delete products
- Manage supplier details
- Add, view, edit, and delete stock records
- Search stock by product name
- Low stock alerts for products with quantity of 10 or less
- Responsive interface using HTML and CSS

## Technologies Used
- Python
- Django
- SQLite
- HTML
- CSS

## Installation
1. Clone or download this project.
2. Open the project folder in the terminal.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate the virtual environment:
   `.\.venv\Scripts\Activate.ps1`
5. Install Django:
   `python -m pip install django`
6. Apply migrations:
   `python manage.py migrate`
7. Start the development server:
   `python manage.py runserver`
8. Open `http://127.0.0.1:8000/` in your browser.

## Run Tests
`python manage.py test products`

## Developer
Sanjaiya S
