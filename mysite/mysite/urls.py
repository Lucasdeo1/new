from django.urls import path
from usuarios import views

urlpatterns = [
    path('usuarios', views.cadastrar_usuario, name='cadastrar_usuario'),

]

