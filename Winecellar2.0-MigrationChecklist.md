Winecellar2.0 Migration

## Database

    Rename table wine_ to wines_




## Path in settings.py

    STATIC_URL = '/static/'
    #STATIC
    LOGIN_REDIRECT_URL = '/wines'
    LOGOUT_REDIRECT_URL = '/'
    LOGIN_URL = '/login/'


Disable:
 ~~   #'django.contrib.admin', ~~
in apps