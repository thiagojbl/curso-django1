pip install --upgrade pip
pip install -r requirements.txt
useradd thiago
chown -R thiago:thiago /code/project
chown -R thiago:thiago /code/manage.py
# pip3 install psycopg2-binary 
python manage.py runserver 0.0.0.0:8000 
