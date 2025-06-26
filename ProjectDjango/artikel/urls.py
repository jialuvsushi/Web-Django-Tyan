from django.urls import path
from . import views
from artikel.views import (
    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,
)

urlpatterns = [
    path('kategori/list', admin_kategori_list, name='admin_kategori_list'),
    path('kategori/tambah', admin_kategori_tambah, name='admin_kategori_tambah'),
    path('kategori/update/<int:id_kategori>', admin_kategori_update, name='admin_kategori_update'),
    path('kategori/delete/<int:id_kategori>', admin_kategori_delete, name='admin_kategori_delete'),

    path('artikel', views.artikel_list, name='admin_artikel_list'),
    path('artikel/tambah/', views.artikel_tambah, name='artikel_tambah'),
    path('artikel/edit/<int:id_artikel>/', views.artikel_update, name='artikel_update'),
    path('artikel/hapus/<int:id_artikel>/', views.artikel_delete, name='artikel_delete'),
    ]
