from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nama

class ArtikelBlog(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    konten = RichTextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='gambar_artikel/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.judul

class Komentar(models.Model): 
    ArtikelBlog = models.ForeignKey(ArtikelBlog, on_delete=models.CASCADE, related_name='komentar') 
    nama = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Komentar oleh {self.nama} pada {self.ArtikelBlog.judul}"