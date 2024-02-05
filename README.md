скачать проект git clone https://github.com/AlenaSapfirova/task

Создать файл .env
```
touch .env
```
Заполнить по аналогии с .env.example

## Запуск проекта на локальной машине Linux

* Создать виртуальное окружение и активировать его
* Установить зависимости
```
sudo apt update
sudo apt install python3.10-venv
python3.10 -m vevn venv
source venv/bin/activate
pip install -r requirements.txt
```
* Создать базу данных в postgres
```
sudo apt install postgresql postgresql-contrib -y
sudo -u postgres psql
CREATE DATABASE task;
# Cоздать своего пользователя или пропустить этот шаг и рабоать с postgres
```
* Установите Redis в качестве брокера Celery и серверной части базы данных
```
sudo apt install redis
```
* Запустить сервер в терминале `redis-server`
* В другом терминале(2) перейти в папку `task` и запустить celery
```
cd wellcards
python -m celery -A task worker -l info -B # флаг -B только для linux
```
* В первом терминале запустить сервер Django + cделать миграции
```
cd wellcards
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Запустить локально docker-compose up



