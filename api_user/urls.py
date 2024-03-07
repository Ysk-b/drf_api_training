from rest_framework.routers import DefaultRouter
from django.urls import path, include

# 以下を記載することで、api_user/urls.pyでrouterをインポートすることができる
app_name = 'api_user'
router = DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
]