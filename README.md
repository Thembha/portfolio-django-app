# portfolio-django-app

This repo is for a Django based portfolio app.

# Tech Stack

1. Python 3
2. Django
3. PostgreSQL
4. JavaScript
5. Leaflet.js

# Requirements

All dependencies are stored in the requirements.txt file. It's best to have a virtual environment for the project and to use pip to install the said requirements within the environment.
<br><br>

# Running the System

<h3>A Few Assumptions:</h3>
You have ...
<ul>
    <li>PostgreSQL installed</li>
    <li>Django installed</li>
    <li>created a postgreSQL database for the project</li>
</ul><br>

<h3>Must do:</h3>
<ul>
    <li>Use the '.env.example' file as a template for your '.env' file.</li>
    <li>Have your db connection variables added into your '.env' file according to the example</li>
    <li>Run 'python manage.py migrate' to add necessary tables to your DB</li>
    <li>Run 'python manage.py createsuperuser' to create a new super user for the system</li>
    <li>Run 'python manage.py runserver' to run the system</li>
</ul>
<br><br>

# Possible Problems

You will experience problems running this system if: 
<ul>
    <li>you have not intalled all requirements</li>
    <li>the '.env' file is not setup properly.</li>
    <li>you did not run the migration command</li>
    <li>a super user has not been added (you cannot login without a user in the database. Duh!)</li>
</ul>

# Tests

Tests still need to be added. There is currently one test for the models contained in 'tests.py' unser the 'users' app.<br>
Continuous intergration (CI) is not yet done.<br>


# Other Todos

<ul>
    <li>Logging user login/logout activity on the admin page.</li>
    <li>Allowing map location selection on registration and profile editing.</li>
    <li>Beautifying the system, especially the authentication pages.</li>
</ul>