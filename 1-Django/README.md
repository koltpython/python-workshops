# 1. Introduction to Django - Fırat Tamur - 02.12.2019

Short description of used technologies and purpose of the workshop.

This workshop provides a sample of how [Django Framework](https://www.djangoproject.com/) can help you build Web applications using Python. Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. In this workshop, we will create a blog site with Django framework then deploy our site on the pythonanywhere.com website with a free account.

## What you'll build

You'll build a simple personal blog using Django Framework and publish it. You'll create and update your posts in your blog with django admin panel.

[Kolt Django Example Blog Site](https://koltdjangoworkshop.pythonanywhere.com)

## What you'll need

You'll need basic Python and HTML knowledge.

### Installations

You will need Python 3.6+ and python's venv and django packages. To install python packages we'll use the pip. Pip and venv are already installed in Python.

After activating venv:

Run `$ pip install django`

### Starter Code

After install the Django:

To start a new Django Project:

Run `$ django-admin startproject project_name`

To test initialization of project go to project folder:

Run `$ python manage.py runserver`

To start a Django App:

Run `$ python manage.py startapp app_name`


### Presentation

[Presentation Link](https://drive.google.com/file/d/11-geg--0mFDU9kqYFL9QuibQh552qvqr/view?usp=sharing)

## 1. Create a Virtual Environment(venv)

To create a new venv for tutorial:

Run `$ python3 -m venv tutorial-env`

// in mac and linux

Run `$ source tutorial-env/bin/activate` 

// in windows

Run `$ tutorial-env\Scripts\activate.bat`

## 2. Install Required Packages Using pip 

If you have a requirements.txt a project to install all packages used in project:

Run `$ pip install -r requirements.txt`

## 3. Run the starter project.

If you want to use that project, you can simply download and work on the project. After you install the project, you have to create a venv and install the packages inside the requirements.txt. 

## Summary

This workshop aims to show how can Python be used in different areas. In this workshop, Python is used to create a blog website with Python's Django Framework. Django is a great Python framework that provides programmers to create complex websites in python with less code.

## Links

Links to get more information about the demo, tools, other guides, etc.

- [Instructor's Personal Blog](https://tamurfirat.pythonanywhere.com/)
- [Django Framework Website](https://www.djangoproject.com/)
- [Django Tutorial by Django Girls](https://tutorial.djangogirls.org/)


