from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# let's wire up the API with automatic URL routing
# we'll also include login URLs for the browsable API

app_name = 'rest_API'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
