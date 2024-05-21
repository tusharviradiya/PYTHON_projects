# PYTHON_projects
python project basic to advance

# installation part

- pipenv shell

- pip install django

- Project create
	django-admin startproject texttoimg
	cd texttoimg/
	django-admin startapp text_to_img_app //-> Create App
	python3 manage.py runserver

- bootstrap installation : install manualy from website

- install font awesome : install from their site

- Migration:
- python3 manage.py makemigrations
- python3 manage.py migrate

#### we build project and after that we need to host out projet so here are some steps which we need to follow

1. command for save package installed in our project
- pip freeze ( for list of installed package)
- pip freeze > package.txt

2. after that we need to conver our project into zip file

3. visit pythonanywhere
- create account
- upload zip file
- open console and create virtual env
- create web App
- give env name to virtual section
- 