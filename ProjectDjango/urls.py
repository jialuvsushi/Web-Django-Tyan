from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from artikel import views
from ProjectDjango.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page dan umum
    path('', views.home, name='home'),
    path('about/', views.about_author, name='about_author'),
    path('artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),
    path('artikel_list/', views.artikel_list, name='artikel_list'),

    # Dashboard dan artikel
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', include('artikel.urls')),  

    # Auth
    path('auth-login/', login, name='login'),
    path('auth-logout/', logout, name='logout'),
    path('auth-registrasi/', registrasi, name='registrasi'),

    # CKEditor 
    # path('ckeditor/', include('ckeditor_uploader.urls')),  
]

# Untuk development (akses media dan static file)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)