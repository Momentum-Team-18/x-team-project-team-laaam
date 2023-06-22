from django.urls import path
from cards import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='home')
]
