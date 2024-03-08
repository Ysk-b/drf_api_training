from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_dm import views

# 以下を記載することで、api_user/urls.pyでrouterをインポートすることができる
app_name = 'api_dm'
router = DefaultRouter()
router.register('message', views.MessageViewSet, basename="message")
router.register('inbox', views.InboxListView, basename='inbox')

urlpatterns = [
    path('', include(router.urls)),
]