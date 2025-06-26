from django.contrib import admin
from .models import ArtikelBlog, Kategori, Komentar


class KomentarAdmin(admin.ModelAdmin):
    list_display = ['nama', 'isi', 'ArtikelBlog', 'tanggal']
    search_fields = ['nama']
    list_filter = ['ArtikelBlog']

class ArtikelBlogAdmin(admin.ModelAdmin):
    list_display = ('kategori', 'judul', 'status')
    search_fields = ('judul',)
    list_filter = ('status', 'kategori')
    list_per_page = 10

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'created_at', 'created_by')
    search_fields = ('nama',)


admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Komentar, KomentarAdmin)
admin.site.register(ArtikelBlog, ArtikelBlogAdmin)
