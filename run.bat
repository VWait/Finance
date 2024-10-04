pip install -r requirements.txt
cd finance
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
