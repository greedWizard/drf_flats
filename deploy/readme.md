Запуск

TODO: перенесети данные для авторизации бд в перменные среды

Deploy dev:

```
sudo apt-get install docker docker-compose

cd deploy

docker-compose build && docker-compose up
```

Добавить область

С запущенными контейнерами:

```
docker ps # узнать id контейнера

docker exec -it <id контейнера> addstate 
```

Добавить город

```
docker ps # узнать id контейнера

docker exec -it <id контейнера> addcity 
```

Миграции

```
docker ps # узнать id контейнера

docker exec -it <id контейнера> python manage.py makemigrations

docker exec -it <id контейнера> python manage.py migrate
```

Документация drf_spectacular:

/api/v1/schema/docs/#/