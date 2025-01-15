<!-- install virtual env -->
pip install virtualenv

<!-- crete virtualenv -->
virtualenv env_file
python -m virtualenv env_file

<!-- activate virtualenv -->
env\Scripts\activate

<!-- install django -->
pip install django

<!-- start project -->
django-admin startproject project_name . 
django-admin startproject project_name

<!-- run server -->
python manage.py runserver

<!-- start app -->
python manage.py startapp app_name

<!-- to create migrations files  -->
python manage.py makemigrations

<!-- to implement the migrations files -->
python manage.py migrate

<!-- create a user -->
python manage.py createsuperuser