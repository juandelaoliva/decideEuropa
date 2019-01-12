=====
Authentication
=====

Authentication is a simple Django for users can be logged
in the proyect

Quick start
-----------

1. Add "autentication" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'authentication',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('authentication/', include('authentication.urls')),

3. Run `python manage.py migrate` to create the polls models.