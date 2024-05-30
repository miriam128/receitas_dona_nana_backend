#Ambiente de desenvolvimento

##Criar ambiente virtual
py -m venv venv
##Iniciar ambiente virtual:
./venv/Scripts/activate

##Rodar migrations
python manage.py migrate

##Super user database
python manage.py createsuperuser
user: admin
password: 123456

##Rodar servidor
python manage.py runserver

##tutorial
https://youtu.be/Q2tEqNfgIXM