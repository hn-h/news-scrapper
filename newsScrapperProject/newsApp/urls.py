from django.urls import path, include
from rest_framework import routers
from newsApp import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsAPIView)

urlpatterns = [
  path('', views.scrape, name="scrape"),
  path('api/', include(router.urls)),
]
