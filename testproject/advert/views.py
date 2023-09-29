from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .models import Advert
from .serializers import AdvertSerializer

class AdvertList(APIView):
    def get(self, request, format = None):
        adverts = Advert.objects.all()
        serializer = AdvertSerializer(adverts, many = True)
        return Response(serializer.data)

class AdvertDetail(APIView):
    def get_advert(self, pk):
        try:        
            return Advert.objects.get(pk=pk)
        except Advert.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        advert = self.get_advert(pk)
        serializer = AdvertSerializer(advert, many = False)
        advert.views += 1
        advert.save()
        return Response(serializer.data)
