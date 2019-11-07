# Wine App Project with Django

### Run testserver

     python manage.py runserver

# Install Django project on IDE from github repo

- Clone repo

- Create virutal env
    
       python3 -m venv wine-env
       
- Activate virtual env wine-env

        source wine-env/bin/activate
        
- Install Django

        pip install django
        
        
       
- Install Watson Search engine
    https://github.com/etianen/django-watson/wiki   

        pip install django-watson
        python manage.py runserver
        python manage.py migrate
        python manage.py installwatson
        python manage.py buildwatson
