# cozylibrary



## How To Setup on Windows

1. Clone This Project `git clone https://github.com/dapoadedire/django-blog.git`
2. Go to Project Directory `cd django-blog`
3. Generate a SECRET_KEY with this command `python3 -c 'import secrets; print(secrets.token_hex(100))'`
4. Create a `.env` file and put the generated SECRET_KEY inside.(Check env.example for an example.)
5. Create a Virtual Environment `python -m virtualenv venv`
6. Activate Virtual Enviromment ` venv\Scripts\activate`
7. Install Requirements Package `pip install -r requirements.txt`
8. Migrate Database `python manage.py migrate`
9. Create Super User `python manage.py createsuperuser`
10. Finally Run The Project `python manage.py runserver`


## How To Setup On Linux
1. Clone This Project `git clone https://github.com/dapoadedire/django-blog.git`
2. Go to Project Directory `cd django-blog`
3. Generate a SECRET_KEY with this command `python3 -c 'import secrets; print(secrets.token_hex(100))'`
4. Create a `.env` file and put the generated SECRET_KEY inside.(Check env.example for an example.)
5. Create a Virtual Environment `python -m virtualenv venv`
6. Activate Virtual Environment `source venv/bin/activate`
7. Install Requirements Package `pip install -r requirements.txt`
8. Migrate Database `python manage.py migrate`
9. Create Super User `python manage.py createsuperuser`
10. Finally Run The Project `python manage.py runserver`




This is a library app created with Django.

## Homepage with demo cover images.
![image](https://user-images.githubusercontent.com/95668340/169707970-43dca465-a8bb-4177-bd1c-89a09a8fd5c8.png)

## About page

![image](https://user-images.githubusercontent.com/95668340/169708045-df6fe003-b22b-41b9-a406-2f0db4df796f.png)


## Profile Page

![image](https://user-images.githubusercontent.com/95668340/169708089-1d3d8554-ec90-408b-a483-8d92e6a4f546.png)

## Features

- Download and Upload books by selected users.
- Popular books..
- Books by Category.
- Account Creation.

## Features to be added.

- Reset password option by sending email.
