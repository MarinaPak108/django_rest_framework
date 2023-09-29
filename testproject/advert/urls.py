from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('advert-list/', views.AdvertList.as_view()),
    path('advert/<int:pk>/', views.AdvertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)