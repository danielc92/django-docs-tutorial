# Django Docs Tutorial
Creating a poll application from the official Django documentation site. Might not follow documentation exactly and will make adjustments along the way.
# Before you get started
Concepts/Software/Programming modules a user may have to read up on before getting started with this project. eg. 'Read about [neural networks](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6?gi=44b811975215) before getting started.'

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django-docs-tutorial.git

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
