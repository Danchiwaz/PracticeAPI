from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()
router.register('persons', views.PersonViewSet, basename='persons')


urlpatterns = [
path('viewset/', include(router.urls), name="persons"),
]