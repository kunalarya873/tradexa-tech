CRUD Application with Django REST Framework
===========================================

Project Overview
----------------

This project is a CRUD (Create, Read, Update, Delete) application built with Django REST Framework (DRF). The application manages three resources: **Users**, **Products**, and **Orders**, each stored in separate SQLite databases. It includes validation logic and custom business rules to ensure data integrity and proper handling of user requests.

* * *

Features
--------

### Users

*   Fields: `id`, `name`, `email`
*   Validations:
    *   Email addresses must be valid.
*   Endpoints:
    *   `GET /api/users/` - List all users.
    *   `POST /api/users/` - Create a new user.
    *   `GET /api/users/{id}/` - Retrieve a user by ID.
    *   `PUT /api/users/{id}/` - Update a user by ID.
    *   `DELETE /api/users/{id}/` - Delete a user by ID.

### Products

*   Fields: `id`, `name`, `price`
*   Validations:
    *   Price must be non-negative.
*   Endpoints:
    *   `GET /api/products/` - List all products.
    *   `POST /api/products/` - Create a new product.
    *   `GET /api/products/{id}/` - Retrieve a product by ID.
    *   `PUT /api/products/{id}/` - Update a product by ID.
    *   `DELETE /api/products/{id}/` - Delete a product by ID.

### Orders

*   Fields: `id`, `user_id`, `product_id`, `quantity`
*   Validations:
    *   Quantity must be greater than zero.
    *   User and product must exist in their respective databases.
*   Endpoints:
    *   `GET /api/orders/` - List all orders.
    *   `POST /api/orders/` - Create a new order.
    *   `GET /api/orders/{id}/` - Retrieve an order by ID.
    *   `PUT /api/orders/{id}/` - Update an order by ID.
    *   `DELETE /api/orders/{id}/` - Delete an order by ID.

* * *

Installation and Setup
----------------------

### Prerequisites

*   Python 3.10+
*   Django 4.x
*   Django REST Framework
*   SQLite3

### Setup Instructions

1.  **Clone the Repository:**
    
    `git clone https://github.com/kunalarya873/tradexa-tech`
    
    `cd tradexa-tech` 
    
2.  **Create and Activate a Virtual Environment:**
    
    `python -m venv venv`

    `source venv/bin/activate  # On Windows: venv\Scripts\activate` 
    
3.  **Install Dependencies:**
    
    `pip install -r requirements.txt` 
    
4.  **Set Up Databases:** Run migrations for each database:
    
    `python manage.py migrate --database=users`

    `python manage.py migrate --database=products`
    
    `python manage.py migrate --database=orders` 
    
5.  **Run the Development Server:**
    
    `python manage.py runserver` 
    
6.  **Access the API:** The API is available at `http://127.0.0.1:8000/api/`.
    

* * *

How to Use the API
------------------

You can interact with the API using tools like **Postman**, **cURL**, or your web browser. Below are examples of creating records:

### Create a User

**POST /api/users/**

`{
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
}` 

### Create a Product

**POST /api/products/**

`{
    "id": 1,
    "name": "Laptop",
    "price": 1000.00
}` 

### Create an Order

**POST /api/orders/**

`{
    "id": 1,
    "user_id": 1,
    "product_id": 1,
    "quantity": 2
}` 

* * *

Validation and Business Rules
-----------------------------

*   **Users:** Email validation ensures proper formatting.
*   **Products:** Prices must be non-negative.
*   **Orders:**
    *   Quantity must be greater than zero.
    *   User and product must exist in their respective databases.

* * *

Future Enhancements
-------------------

*   Add filtering and pagination to the endpoints.
*   Include product stock management for orders.
*   Implement authentication and authorization for API endpoints.

* * *

License
-------

This project is licensed under the MIT License.

* * *

Contact
-------

For any questions or suggestions, feel free to contact:  
**Kunal**  
_Full-Stack Web Developer_  
\[kunalarya873@gmail.com\]
