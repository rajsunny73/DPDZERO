
# API DEPLOYMENT

A brief description of what this project does and who it's for


## Framework CHOICE

We have chosen the Django framework to build this project. Django is a powerful Python web framework that provides a robust set of tools for building web applications, including a powerful ORM (Object-Relational Mapping) system, built-in authentication, and a customizable admin interface. It is a great choice for developing web applications quickly and efficiently.

## DATABASE SCHEMA

For this project, we have used the built-in SQLite database that comes with Django by default. The database schema consists of tables and relationships defined in Django models. These models are located in the models.py file of the Django app, and they define the structure of the database.
## Instructions to Run the code

To run this code on your local machine, follow these steps:

Clone the project repository from GitHub.

```bash
git clone https://github.com/rajsunny73/DPDZERO
```
```bash
Navigate to the project directory.
cd yourproject
```
Create a virtual environment (optional but recommended).
```bash
python -m venv venv
```

Apply database migrations.
```bash
python manage.py makemigrations
python manage.py migrate
```
Run the development server.

```bash
python manage.py runserver
Access the application in your web browser at http://localhost:8000/.
```
Endpoints
```bash
/admin/
for admin pannel

/api/register/
for registered user database

/api/token/
for token generated list

/api/storage/
for storage data

/api/storage/(for further access of data write the key name)
```
## Instructions to Set Up the Code

To deploy this project run

```bash

Clone the project repository from GitHub as mentioned in step 1 of the "Instructions to Run the Code" section.
```
```bash
Navigate to the project directory as mentioned in Instructions to run the code.
```
```bash
Install the required dependencies as mentioned in Instructions to run the code.
```
```bash
Customize the Django settings according to your needs. Modify the settings.py file in the project's root directory to configure database settings, secret key, allowed hosts, and other project-specific settings.
```
```bash
Configure any environment variables required for your project, such as API keys, secret tokens, or other sensitive information.
```
```bash
Apply database migrations use
python manage.py makemigrations
python manage.py migrate
```
```bash
Run the development server as "python manage.py runserver"
configure your production server environment for deployment.
```

```bash
With these instructions, you should be able to run and set up the Django project successfully. Feel free to reach out for further assistance or clarification.
```

