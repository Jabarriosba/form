from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('registro/', views.registro_list, name='registro_list'),
    path('registro/create/', views.registro_create, name='registro_create'),
    path('registro/update/<int:id>/', views.registro_update, name='registro_update'),
    path('registro/delete/<int:id>/', views.registro_delete, name='registro_delete'),
    path('registro/json/', views.registro_list_json, name='registro_list_json'),
]
