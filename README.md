[TOC]
### Wine App Project with Django

#### Run testserver

     python manage.py runserver

     run from remote: python3 manage.py runserver 0.0.0.0:8000
    
#### Install Django project on IDE from github repo
    # Clone repo

    # Create virutal env
    python3 -m venv wine-env
       
    # Activate virtual env wine-env
    source wine-env/bin/activate
        
    # Install Django
    pip install django

#### Run app with gunicorn / wsgi package
    # Install gunicorn package
    pip install gunicorn
    
    # Copy wsgi.py file into repo directory
    cd /opt/django-winecellar
    cp wineproject/wsgi.py .
    
    # Activate virtual env
    source wine-env/bin/activate
    
    # Start gunicorn server
    cd /opt/django-winecellar
    gunicorn -b 0.0.0.0:8000 wsgi:application &
        
#### Links/Helps/Tutorials:
- User Authentication
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication


#### Not implemented:
- ~Search~
- ~Column filter~
- Auth -> Users / Group users
- ~Edit date in detail view~
- PDF export 
- Excel export
- ...

#### Increase sqlite version on CentOS
    # Get the current sqlite version on CentOS:
    cd /tmp
    wget https://www.sqlite.org/2019/sqlite-tools-linux-x86-3300100.zip
    unzip sqlite-tools-linux-x86-3300100.zip
    which sqlite3
    cd /tmp/sqlite-tools-linux-x86-3300100
    cp sqlite3 /usr/bin/sqlite3

    yum install glibc.i686
    yum -y install libz.so.1

    # Check:
    sqlite3
    SQLite version 3.30.1 2019-10-10 20:19:45
