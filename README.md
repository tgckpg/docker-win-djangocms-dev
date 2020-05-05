# docker-win-djangocms-dev
A kickstart repo for Django CMS using Docker for Windows. For development only.

## Bulid & Start
Go inside `/docker-win`, then run
```
docker-compose build
docker-compose up
```

## Initialize tables & collectstatic
```
docker exec -it windev_web python /Code/src/manage.py makemigrations
docker exec -it windev_web python /Code/src/manage.py migrate
docker exec -it windev_web python /Code/src/manage.py collectstatic --no-input
```

### Create root account for django admin
```
docker exec -it windev_web python /Code/src/manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.create_superuser( 'root', 'www@example.com', 'my-very-awesome-password-long-eh?' )
>>>
```
