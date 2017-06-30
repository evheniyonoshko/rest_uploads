This is django REST full api

At first clone this project to your local machine
git clone https://github.com/evheniyonoshko/rest_uploads.git

Than go to the project dir ('cd rest_uploads'), create virtualenv, and install requirements.txt ("pip install -r requirements.txt")

Then you need to create database and put your database name ('NAME'), user name ('USER'), password ('PASSWORD') to DATABASES in settings.py file. 
It look like this: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db_name',
            'USER': 'db_user',
            'PASSWORD': 'user_password',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }

After that run makemigrations command ('./manage.py makemigrations uploads') and migrate command ('./manage.py migrate')

Than you need create superuser ('./manage.py createsuperuser')

Run server ('./manage.py runserver')

Open new terminal

Only authorizated users can save data, and at first you can authorizated with username and password that you olready create('./manage.py createsuperuser')
For authorization post data with username and password:

curl -d "username=your_username&password=your_password" http://127.0.0.1:8000/api-token-auth/login/

After that you will get authorization token (like this '18879d49a02d0deec7f2752bb25ed5bed45c70c7')

If you want to send your file you need to post data with your authorization token, path to file and description for this file:

curl -X POST http://127.0.0.1:8000/api/uploads/ -H 'Authorization: Token {your authorization token}' -F file=@/home/example.log -F description="description for this file"

Than you will get saved data with key:
{
    "description":"hello this is my first post", "file":"http://127.0.0.1:8000/media/files/example.log",
    "key":"YGmSTH6HoskXi6Td"
}

You can get all your posted data one by one if you add key to url /api/uploads/{key}:

curl -H 'Authorization: Token 18879d49a02d0deec7f2752bb25ed5bed45c70c7' http://localhost:8000/api/uploads/YGmSTH6HoskXi6Td/

You can delete your file:
curl -H 'Authorization: Token 18879d49a02d0deec7f2752bb25ed5bed45c70c7' -X DELETE http://localhost:8000/api/uploads/YGmSTH6HoskXi6Td/
