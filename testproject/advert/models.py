from django.db import models
from django.db.models import UniqueConstraint, Index
from datetime import date, time, datetime
import datetime

class Category(models.Model):
	name = models.CharField(max_length = 254, unique = True)


class City(models.Model):
	name = models.CharField(max_length = 254, unique = True)


class Advert(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 500, blank = True, default = "")
	description = models.CharField(max_length = 1000)
	views = models.BigIntegerField(default = 0, editable = False)
	city = models.ForeignKey(City, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	class Meta:
		ordering = ["created"]
		constraints = [
			models.UniqueConstraint(fields = ["created", "title"], name = "unique_advert")
		]
		

