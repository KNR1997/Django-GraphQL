# Django GraphQL Project

This project is a backend application built for an ecommerce application using Django and GraphQL. It provides a flexible and efficient API interface, enabling users to query and manipulate data with precision.

## Features

- **GraphQL API**: Integrated with Django using `Graphene-Django`.
- **Authentication**: Token-based authentication for secure access.
- **CRUD Operations**: Full support for Create, Read, Update, and Delete operations via GraphQL queries and mutations.
- **Scalable Architecture**: Modular and extendable design for adding new features.

---

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KNR1997/Django-GraphQL.git
   cd Django-GraphQL

2. Setup a virtual environment:
   ```bash
   pip install virtualenv
   virtualenv venv

3. Activate the virtual environment and install requirements:
   ```bash
   venv\scripts\activate
   pip install -r requirements.txt
   
4. Make database migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run application
   ```bash
   python manage.py runserver
