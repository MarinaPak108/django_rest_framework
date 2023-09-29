from rest_framework import serializers
from .models import Advert, City

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ["name"]


class AdvertSerializer(serializers.ModelSerializer):
		city = CitySerializer()
		class Meta:
			model = Advert
			fields = ["id", "title", "created", "description", "views", "city"]
