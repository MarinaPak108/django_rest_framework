# django_rest_framework

- Django==4.2.5
- djangorestframework==3.14.0
- mysqlclient==2.2.0

models:

Category - filed:name
City - field: name
Advert - field: created, title, description, city (fk), category(fk), views (counter)

views:

/api/advert-list/ - json list of all adverts
/api/advert/<advert-pk>/ - json detail view of selected view (views counter)


Dockerfile (MySQL locally)
Docker-compose (MySQL image)
