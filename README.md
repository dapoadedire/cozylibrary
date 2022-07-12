# Cozy Library

Cozy Library is a web app that allows users to download books of different genres, and allows selected users to upload books.


## Author

- [@dapo_adedire](https://www.twitter.com/dapo_adedire)



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`DEBUG`

`EMAIL_BACKEND`
`EMAIL_HOST_USER`
`EMAIL_HOST`
`EMAIL_PORT`
`EMAIL_HOST_PASSWORD= ''  # TODO: Give APP Password here`
`EMAIL_USE_TLS`
`EMAIL_TIMEOUT`

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
python manage.py migrate
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


## Support

For support, email adedireadedapo19@gmail.com or send a Twitter DM @ twitter.com/dapo_adedire.
Also, this project needs a star from you.


## Tech Stack

**Client:** HTML, CSS, BootstrapCSS, Javascript

**Server:** Django, SQL


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Screenshots


### Homepage with demo cover images.
![image](https://user-images.githubusercontent.com/95668340/169707970-43dca465-a8bb-4177-bd1c-89a09a8fd5c8.png)

### About page

![image](https://user-images.githubusercontent.com/95668340/169708045-df6fe003-b22b-41b9-a406-2f0db4df796f.png)


### Profile Page

![image](https://user-images.githubusercontent.com/95668340/169708089-1d3d8554-ec90-408b-a483-8d92e6a4f546.png)

### Features

- Download and Upload books by selected users.
- Popular books..
- Books by Category.
- Account Creation.

### Features to be added.

- Reset password option by sending email.
