===========
Geologysite
===========

Geologysite is a simple Django app and my first django app))).

Python ==3.6;
Django ==2.1.3


Quick start
-----------

1. Install package in your django project using 'pip install git+https://github.com/kare1ov/django-geologysite.git', or you can download 'django-geologysite-0.1.tar.gz' from 'dist' folder and install package using 'pip install <path_to_file/django-geologysite-0.1.tar.gz'.


2. In your_project/settings.py add "geologysite" and other dependencies to your INSTALLED_APPS setting, add url to redirect after login to your LOGIN_REDIRECT_URL,
   add path for your static and media files like this::

    INSTALLED_APPS = [
        ...
        'geologysite',
        'bootstrapform',
        'ckeditor',
        'ckeditor_uploader',
    ]


    LOGIN_REDIRECT_URL = 'home_page'



    # Static files (CSS, JavaScript, Images)

    STATIC_URL = '/static/'
    STATIC_ROOT = 'static'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'media'


    CKEDITOR_UPLOAD_PATH = "uploads/"

3. Include the geologysite URLconf in your project urls.py like this::

    path('Your_url', include('geologysite.urls')),

4. Run `python manage.py migrate` to create the geologysites models.

5. Create superuser using 'python manage.py createsuperuser'.

6. Start the development server 'python manage.py runserver' and visit http://127.0.0.1:8000/admin/
   to create a first entry in your database. Minerals and Rock entries can create only admin, Article can create Admin and each user which are registered in website.

7. Visit http://127.0.0.1:8000/Your_url/ .
