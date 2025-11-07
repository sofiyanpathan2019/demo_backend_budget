1.Create and activate virtual environment
  cd backend
  python -m venv venv
  source venv/bin/activate       # macOS/Linux
  venv\Scripts\activate          # Windows


2.Install Requirements
  pip install -r requirements.txt

3.Add database
  DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'expense_db',
    'USER': 'postgres',
    'PASSWORD': 'yourpassword',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}


4.Migrate into database
  python manage.py makemigrations
  python manage.py migrate


5.python manage.py runserver
