# urls.py
from django.urls import path
from django.views import View
from . import views
from .views import home_view, CrearPost, ListarPost, EliminarPost, DetallePost, EditarPost

urlpatterns = [
    path('', home_view, name='home'),
    path('crear_post/', CrearPost.as_view(), name='crear_post'),
    path('listar_post/', ListarPost.as_view(), name='listar_post'),
    path('detalle_post/<int:pk>/', DetallePost.as_view(), name='detalle_post'),
    path('editar_post/<int:pk>/', EditarPost.as_view(), name='editar_post'),
    path('eliminar_post/<int:pk>/', EliminarPost.as_view(), name='eliminar_post'),
]