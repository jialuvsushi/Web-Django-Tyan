# ProjectDjango/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from artikel import views
from ProjectDjango.authentication import login, logout, registrasi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),
    path('about/', views.about_author, name='about_author'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('artikel_list', views.artikel_list, name='artikel_list'),

############################ Authentication ################################
    path('auth-login',login, name='login'),
    path('auth-logout',logout, name='logout'),
    path('auth-registrasi',registrasi, name='registrasi'),


    path('dashboard/', include("artikel.urls")),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
