# HR Management System (HRMS)

This project is a Human Resource Management System (HRMS) built using Django, PostgreSQL, and Docker. It provides features for both admin and client users to manage various HR-related tasks efficiently.

## Features

- **Admin Features**: Manage employee records, departments, roles, and other HR functionalities.
- **Client Features**: Employees can view their profiles, submit requests, and access relevant information.

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- PostgreSQL: A powerful, open-source object-relational database system.
- Docker: Containerization platform to simplify deployment and management of applications.

## Project Structure

```
hrms-project
├── hrms
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── admin
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── client
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd hrms-project
   ```

2. **Create a `.env` file**:
   Populate the `.env` file with your database credentials and secret keys.

3. **Build and run the Docker containers**:
   ```
   docker-compose up --build
   ```

4. **Run migrations**:
   ```
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser**:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application**:
   Open your browser and navigate to `http://localhost:8000` for the client interface or `http://localhost:8000/admin` for the admin interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# hrms-project
Microsoft Co-Pilate in Action
