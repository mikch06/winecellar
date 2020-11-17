#### Run app with gunicorn / wsgi package
    # Install gunicorn package
    pip install gunicorn
      
    # Activate virtual env
    source wine-env/bin/activate
    
    # Start gunicorn server
    cd /opt/django-winecellar
    <PATH>/gunicorn -b 0.0.0.0:8000 <appname>.wsgi (&)
    (from where manage.py is)
