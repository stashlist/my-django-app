from django.contrib import admin
from django.urls import path
from myapp import views  # `myapp.views` をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # `http://127.0.0.1:8000/` で `index.html` を表示
]
