# Wine App Project with Django

### Run testserver

     python manage.py runserver

     run from remote: python3 manage.py runserver 0.0.0.0:8000
    
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



Links/Helps/Tutorials:
- User Authentication
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication


# Not implemented:
- ~Search~
- Column filter
- Auth -> Users / Group users
- Edit date in detail view
- PDF export 
- Excel export
- ...

