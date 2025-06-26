from django import forms  
from .models import Kategori, ArtikelBlog

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'required' : 'True' 
                }),     
        }

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBlog
        fields = ['judul', 'isi', 'kategori', 'gambar']

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={
                'class': 'ckeditor',
                'id': 'id_isi',
                'class': 'ckeditor',  
            }),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
