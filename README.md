# django_rest_framework

- Django==4.2.5
- djangorestframework==3.14.0
- mysqlclient==2.2.0

models:

Category - категории объявлений, поля: name
City - город объявления, поля: name
Advert - объявление, поля: created (дата создания), title, description, city, category, views

views:

/api/advert-list/ - json список объявлений со всеми полями + название города + название категории
/api/advert/<advert-pk>/ - json detail view одного объявления со всеми полями, просмотр данного вью увеличивает счётчик просмотров в объявлении


Dockerfile (MySQL locally)

additionally
- docker-compose: Project + MySQL virtually
