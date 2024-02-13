
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.button),
    path('output', views.output, name="script"),
    path('external/', views.external),
    path('send/', views.send, name="send"),
]
