*Features 
  CRUD APIs for Expense management
  
  Integration with live Currency API (EUR-based)
  
  All exchange rates normalized to INR base
  
  PostgreSQL as the main database
  
  Django REST Framework for API handling
  
  CORS enabled for frontend communication


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
