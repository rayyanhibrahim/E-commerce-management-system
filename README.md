
E-Commerce Management System (Flask + MongoDB)

Project Overview

The E-Commerce Management System is a simple web-based application developed using Python Flask and MongoDB. The system allows users to manage product information through basic CRUD (Create, Read, Update, Delete) operations.

This project demonstrates how a backend framework can be integrated with a NoSQL database and dynamic frontend templates to build a functional web application.

The application allows users to:

Add new products

View available products

Update existing product details

Delete products from the system


This project was developed as part of a BTech mini project to understand full-stack web development concepts.


---

Technologies Used

Backend

Python

Flask Framework

PyMongo


Database

MongoDB


Frontend

HTML

Jinja2 Template Engine


Development Tools

Visual Studio Code

Web Browser



---

Project Features

Product management system

Full CRUD operations

Dynamic HTML rendering using Jinja2

MongoDB database integration

Simple and user-friendly interface

Lightweight Flask architecture



---

Project Structure

Ecommerce-Management-System
│
├── app.py
├── requirements.txt
│
├── templates
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
└── README.md

File Description

app.py
Main Flask application containing routes and database operations.

templates/
Folder containing all frontend HTML pages.

index.html
Displays the list of products stored in the database.

add.html
Form used to add a new product.

edit.html
Form used to update existing product details.


---

CRUD Operations

Create

Adds a new product to the database.

collection.insert_one()

Read

Retrieves product data from the database.

collection.find()

Update

Updates existing product information.

collection.update_one()

Delete

Removes a product from the database.

collection.delete_one()


---

How to Run the Project

1. Clone the Repository

git clone https://github.com/yourusername/ecommerce-management-system.git

2. Install Required Libraries

pip install -r requirements.txt

3. Start MongoDB Server

Make sure MongoDB is installed and running on your system.

4. Run the Flask Application

python app.py

5. Open in Browser

http://127.0.0.1:5000


---

Advantages of the System

Easy to understand structure

Lightweight and fast framework

Demonstrates complete CRUD functionality

Good learning project for beginners

Can be expanded into a full e-commerce system



---

Limitations

No authentication system

Basic user interface

No role-based access control

No order or payment functionality



---

Future Enhancements

User authentication system

Shopping cart functionality

Order management system

Payment gateway integration

Product image upload feature

Search and filtering options

Deployment on cloud platforms



---

Author

Rayyan Ibrahim
BTech 2nd Year
Mini Project – E-Commerce Management System

