## Installation
#### 1. Install python-3.8.11 and mysql-10.4.21

#### 2. Setup virtual environment

```bash
#Install virtual environment
sudo apt install python3-virtualenv

# Create virtual environment
virtualenv env -p python3

# Activate virtual environment
source env/bin/activate
```

#### 3. Clone git repository

```bash
git clone https://github.com/soniya-dhoke/django_learny_webapp
```

#### 4. Install requirements

```bash
cd django_learny_webapp/
pip install -r requirements.txt
```

#### 5. Load sample data into MySQL

```bash
# open mysql bash
mysql -u <mysql-user> -p

# Give the absolute path of the file
mysql> source ~/learny_database.sql
mysql> exit;
```

#### 6. Edit project settings

```bash
# open settings file
vim learny/settings.py

# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learny_database',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}
# save the file
```

#### 7. Run the server

```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
# Now, open your web browser and enter http://127.0.0.1:8000/ to see the website up and running.
```
