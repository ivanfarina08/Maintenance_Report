Abra a pasta backend
cd backend

Criar uma venv
python -m venv venv

ativar venv (Windows)
venv\Scripts\activate

ativar venv (Mac)
source venv/bin/activate

instalar dependencias do arquivo requirements
pip install -r .\requirements.txt

ver quais dependencias estao instaladas na venv
pip freeze

atualizar banco de dados
python manage.py makemigrations
python manage.py migrate

criar um superusuario para o python admin
python manage.py createsuperuser

rodar api
python manage.py runserver

Abra outro terminal e digite 
cd frontend

criar servidor http:
python -m http.server 8080