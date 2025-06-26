from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ArtikelBlog, Kategori
from artikel.forms import KategoriForms

def home(request):
    kategori = Kategori.objects.all()
    kategori_id = request.GET.get('kategori')

    if kategori_id:
        ArtikelBlog_list = ArtikelBlog.objects.filter(kategori__id=kategori_id)
    else:
        ArtikelBlog_list = ArtikelBlog.objects.all()

    print(request.user)
    return render(request, 'home.html', {
        'ArtikelBlog_list': ArtikelBlog_list,
        'kategori': kategori
    })

def detail_artikel(request, id):
    try:
        artikel = ArtikelBlog.objects.get(id=id)
        artikel_lainya = ArtikelBlog.objects.exclude(id=id)[:3]
    except ArtikelBlog.DoesNotExist:
        return render(request, '404_artikel.html')

    return render(request, 'landingpage/detail.html', {
        'artikel': artikel,
        'artikel_lainya': artikel_lainya
    })

def about_author(request):
    return render(request, 'cv.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')

    template_name = "dashboard/index.html"
    context = {
        "title": "selamat datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title": "selamat datang"
    }
    return render(request, template_name, context)

################################# admin ######################################
@login_required(login_url='/auth-login')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori": kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
        return redirect(admin_kategori_list)

    forms = KategoriForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
        return redirect(admin_kategori_list)

    forms = KategoriForms(instance=kategori)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        pass

    return redirect(admin_kategori_list)


#CRUD ARTIKEL

from artikel.forms import ArtikelForms

@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel_list": artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect('admin_artikel_list')
    forms = ArtikelForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            return redirect('admin_artikel_list')

    forms = ArtikelForms(instance=artikel)
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
    except ArtikelBlog.DoesNotExist:
        pass
    return redirect('admin_artikel_list')
