from django import forms  
from artikel.models import Kategori, ArtikelBlog
from ckeditor.widgets import CKEditorWidget

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama": forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'True' 
            }),     
        }

class ArtikelForms(forms.ModelForm):
    konten = forms.CharField(widget=CKEditorWidget()) 

    class Meta:
        model = ArtikelBlog
        fields = ('kategori', 'judul', 'konten', 'gambar', 'status')
        widgets = {
            "kategori": forms.Select(attrs={
                'class': 'form-control',
                'required': 'True' 
            }),   
            "judul": forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'True' 
            }),   
            "gambar": forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "status": forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),           
        }