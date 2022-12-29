# Cozy Library

Cozy Library is a web app where users can download books of different genres.

## Features:

Download books.

Option to view books in category.

Search option.

Sign Up.

Sign In and Sign Out.

Reset and change password options.

## Author

- [@dapo_adedire](https://www.twitter.com/dapo_adedire)

<!-- ## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DEBUG`

`EMAIL_BACKEND`

`EMAIL_HOST_USER`

`EMAIL_HOST`

`EMAIL_PORT`

`EMAIL_HOST_PASSWORD= ''  # TODO: Give APP Password here`

`EMAIL_USE_TLS`

`EMAIL_TIMEOUT` -->
<!--
Check [THIS](https://stackoverflow.com/a/62929967/16006603) out if you're unsure of how to set it up.  -->

## Run Locally

Clone the project

```
  git clone https://github.com/dapoadedire/cozylibrary.git
```

Go to the project directory

```
  cd cozylibrary
```

Create a Virtual Environment

```
python -m virtualenv venv
```

Activate Virtual Environment

```
source venv/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Migrate Database

```
python manage.py migrate accounts
python manage.py migrate cozylibrary
```

Create Super User

```
python manage.py createsuperuser
```

Finally, Start The Server.

```
python manage.py runserver
```

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## Tech Stack

**Client:** HTML, CSS, Javascript

**Server:** Django, SQL

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!--
## Screenshots


### Home
![image](https://user-images.githubusercontent.com/95668340/179268244-7fe50097-be94-4ee0-a1b2-c5f2fcc64381.png)


### Sign Up Page
![image](https://user-images.githubusercontent.com/95668340/179268327-8a1994d1-4e0e-47bb-a9e3-21f315d3fe9c.png)


### Sign In Page
![image](https://user-images.githubusercontent.com/95668340/179268179-94f89a5f-6d17-4b55-a309-64a8d92c9c3c.png)

### User Profile
![image](https://user-images.githubusercontent.com/95668340/179268431-79fc1bf0-0d98-44f9-a6c5-fee155b3f53e.png)

### Password Reset

![image](https://user-images.githubusercontent.com/95668340/179268538-24d53bf5-f348-40b0-b3a0-5ae015a86a58.png)

### Password Reset Email
![image](https://user-images.githubusercontent.com/95668340/179269045-696042f6-4d8b-4869-86ea-ca2d6fc9c987.png)

### Password Change
![image](https://user-images.githubusercontent.com/95668340/179268618-03437619-3716-4c50-83b4-3fcfeeb3f310.png)

### Search Results
![image](https://user-images.githubusercontent.com/95668340/179268834-adbba7dd-d8f0-4177-98e6-a675d8665c42.png)

### Profile Page

![image](https://user-images.githubusercontent.com/95668340/169708089-1d3d8554-ec90-408b-a483-8d92e6a4f546.png) -->

## Support

For support, email adedireadedapo19@gmail.com or send a Twitter DM @ twitter.com/dapo_adedire.
Also, this project needs a star from you.
