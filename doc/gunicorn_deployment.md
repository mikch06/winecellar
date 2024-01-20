#### Run app with gunicorn / wsgi package
    # Activate virtual env
    source wine-env/bin/activate

    # Install gunicorn package
    pip install gunicorn
    
    # Start gunicorn server
    cd /opt/django-winecellar
    <PATH>/gunicorn -b 0.0.0.0:8000 <appname>.wsgi (&)
    (from where manage.py is)
