# Overview

This is an imageboard made with Django. It is a standard singular discussion imageboard. To run the server, create a folder called 'media' in the root and then within media create another folder called 'images'. And then run `python manage.py makemigarations` and `python manage.py migrate`. Then run `python manage.py runserver`.

I made this to familiarize myself with Django and back-end web development.

[Software Demo Video](http://youtube.com)

# Web Pages

The site constists of two dynamically generated web pages: Boards and threads.

The board page showcases the latest 10 threads of that board alongside the latest 5 replies to each thread.

The thread page shows every post for that thread.

# Development Environment

Notepad for Python and CSS, VScode for HTML, cmd prompt for running the Django shell, and git-cli.

This was written in Python with Django.

# Useful Websites

* [Django Docs](https://docs.djangoproject.com/en/3.1/)
* [Stack Overflow](https://stackoverflow.com/)

# Future Work

* Implement bump order
* Add more CSS
* Add tripcodes
