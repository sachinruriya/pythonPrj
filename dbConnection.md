install mysqlclient and pymysql using pip

connection db content --

settings.py
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL backend
        'NAME': 'your_database_name',         # Replace with your database name
        'USER': 'your_database_user',         # Replace with your database user
        'PASSWORD': 'your_database_password', # Replace with your database password
        'HOST': 'localhost',                  # Database server, e.g., '127.0.0.1' or an IP
        'PORT': '3306',                       # Default MySQL port (3306)
    }
}

add code __init__ file --

import pymysql
pymysql.install_as_MySQLdb()


Migration commnads --
python manage.py makemigrations
python manage.py migrate


