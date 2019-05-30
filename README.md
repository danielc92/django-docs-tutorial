# Django Polls App
Creating a poll application from the official Django documentation site. Might not follow documentation exactly and will make adjustments along the way.
# Before you get started
The following concepts are covered in the making of this project.
- Python virtual environments
- Django project configuration
- Django administration
- Dynamic routing
- Template engines
- HTTP/HTTPS methods
- Relational databases
- CRUD operations
- ORM models
- Django deployment to the Cloud
- Responsive web design
- Application security

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django-polls-app.git

```
**Modules/dependencies:**
- `django` (python)
- `Chart.js` (javascript)

Install the following dependences:
```sh
source location-of-venv/bin/activate
pip install django
```

# Tests
- Creating a project
- Creating an app
- Creating an ORM database model for 'Questions' and 'Choices'
- Creating Database using `migrate` and `makemigrations`
- Creating a question (POST)
- Creating choices for a given question (POST)
- Voting for a choice for a given question (POST)
- Accessing the database, making basic crud operations using Django `shell`, as well as admin panel via `localhost:8000/admin`
- Visualizing poll results using horizontal bar chart from Chart.js library

# Contributors
- Daniel Corcoran

# Sources
- [The official Django documentation](https://docs.djangoproject.com/en/2.2/)
- [Chart Js Official site](https://www.chartjs.org/)
