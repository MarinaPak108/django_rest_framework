# django_rest_framework

- Django==4.2.5
- djangorestframework==3.14.0
- mysqlclient==2.2.0

## Models:

Category - filed:name<br>
City - field: name<br>
Advert - field: created, title, description, city (fk), category(fk), views (counter)<br>

## Views:

/api/advert-list/ - json list of all adverts<br>
/api/advert/<advert-pk>/ - json detail view of selected view (views counter)<br>

## Docker
Dockerfile (MySQL locally)<br>
Docker-compose (MySQL image)<br>
