# Ambiente de desenvolvimento

## Criar ambiente virtual
py -m venv venv
## Iniciar ambiente virtual:
./venv/Scripts/activate

## atualizar migrations
python manage.py makemigrations

## Rodar migrations
python manage.py migrate

## Super user
python manage.py createsuperuser
user: admin
password: 123456

## Rodar servidor
python manage.py runserver

## Atualizar requirements.txt
pip freeze > requirements. txt