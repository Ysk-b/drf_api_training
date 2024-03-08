from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen/', views.obtain_auth_token),
    path('api/user/', include('api_user.urls')),
    path('api/dm/', include('api_dm.urls')),
]

# settings.MEDIA_ROOT -> 保存ディレクトリの絶対パス
# settings.MEDIA_URL -> 保存ディレクトリのURLパス
# static -> ファイルのURLパスを追加するための関数
# urlpatterns += static(保存ディレクトリのURLパス, 保存ディレクトリの絶対パス) -> 保存ディレクトリのURLパスを追加
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)