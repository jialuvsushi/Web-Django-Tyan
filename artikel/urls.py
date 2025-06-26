from django.urls import path
from artikel.views import (

    dashboard,

    # Kategori
    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,

    # Artikel
    admin_artikel_list,
    admin_artikel_tambah,
    admin_artikel_update,
    admin_artikel_delete,

    # User Management
    admin_management_user_list,
    admin_management_user_edit,
)

urlpatterns = [
    # Halaman utama dashboard
    path('', dashboard, name='dashboard'),

    # CRUD Kategori
    path('kategori/list/', admin_kategori_list, name='admin_kategori_list'),
    path('kategori/tambah/', admin_kategori_tambah, name='admin_kategori_tambah'),
    path('kategori/update/<int:id_kategori>/', admin_kategori_update, name='admin_kategori_update'),
    path('kategori/delete/<int:id_kategori>/', admin_kategori_delete, name='admin_kategori_delete'),

    # CRUD Artikel
    path('artikel/list/', admin_artikel_list, name='admin_artikel_list'),
    path('artikel/tambah/', admin_artikel_tambah, name='admin_artikel_tambah'),
    path('artikel/update/<int:id_artikel>/', admin_artikel_update, name='admin_artikel_update'),
    path('artikel/delete/<int:id_artikel>/', admin_artikel_delete, name='admin_artikel_delete'),

    # User Management
    path('management-user/list/', admin_management_user_list, name='admin_management_user_list'),
    path('management-user/edit/<int:user_id>/', admin_management_user_edit, name="admin_management_user_edit"),
    path('dashboard/operator/management-user/edit/<int:user_id>/', admin_management_user_edit, name='operator_management_user_edit'),

]