Criar uma venv
python -m venv venv

ativar venv
venv\Scripts\activate

instalar dependencias do arquivo requirements
pip install -r .\requirements.txt

ver quais dependencias estao instaladas na venv
pip freeze

rodar api
python manage.py runserver

atualizar banco de dados
python manage.py makemigrations
python manage.py migrate

criar um superusuario para o python admin
python manage.py createsuperuser
