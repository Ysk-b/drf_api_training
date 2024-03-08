from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'api_user'
router = DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
]