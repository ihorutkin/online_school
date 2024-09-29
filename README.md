# Online english school project

Django project for managing group and lesson in online school

## Check it out

[Online school project deployed to render](https://online-english-school.onrender.com)

## Admin credentials

* login: admin
* password: root1234

## Instalation

Python3 must be already installed

```shell
git clone https://github.com/ihorutkin/online_school.git
cd online_school
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Features

* Authentication for Teacher(Admin)
* Creating, Updating, Deleting of Students, Lessons, Groups
* Ability to register new admin (only admin is able to create new teacher)
* Statistics amount of groups every month