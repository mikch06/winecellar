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