from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  # <– ini penting untuk production
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from artikel import views
from config.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page dan umum
    path('', views.home, name='home'),
    path('about/', views.about_author, name='about_author'),
    path('artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),
    path('artikel_list/', views.artikel_list, name='artikel_list'),

    # Dashboard dan artikel
    path('dashboard/', include('artikel.urls')),  

    # Auth
    path('auth-login/', login, name='login'),
    path('auth-logout/', logout, name='logout'),
    path('auth-registrasi/', registrasi, name='registrasi'),
]

# Untuk staticfiles
urlpatterns += staticfiles_urlpatterns()

# Untuk media files (berfungsi saat DEBUG = False)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Tambahan agar media tetap serve di production (Railway)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]