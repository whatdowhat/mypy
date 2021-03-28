#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'adminweb', #2
        'USER': 'admin', #3                      
        'PASSWORD': 'root',  #4              
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}
SECRET_KEY = 'n7j7dl9^#1xp*zb5gk6#*j!%6jj&6f7h_esjx)k=6iit-qkwp6'
