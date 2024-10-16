from django.shortcuts import render,redirect, get_object_or_404
from .models import Menu
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from .forms import CoffeesForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def homepage(request):
    context = {
        'home' : True
    }
    return render(request, 'homepage/index.html', context)

def about(request):
    context = {
        'about' : True
    }
    return render(request, 'homepage/about.html', context)

def menu(request):
    context = {
        'menu' : True
    }
    return render(request, 'homepage/menu.html', context)

def CRUD_Coffee(request):
    coffee = CRUD_Coffee.objects.all()  # Mengambil semua data game
    return render(request, 'homepage/CRUD_Coffees.html', {'menus': coffee})

def CRUD_Coffee(request):
    query = request.GET.get('q')  # Mencari query dari GET request
    if query:
        coffee = Menu.objects.filter(
            Q(name__icontains=query) |  # Ganti 'name' dengan 'title'
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
    else:
        coffee = Menu.objects.all()  # Ambil semua data coffee
    
    return render(request, 'homepage/CRUD_Coffees.html', {'menus': coffee, 'query': query})

# Add Game
def add_coffee(request):
    if request.method == 'POST':
        form = CoffeesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coffee berhasil dibuat!')
            return redirect('CoffeeList')
        else:
            messages.error(request, 'Terjadi kesalahan saat menambahkan coffee. Silakan periksa input Anda.')  # Pesan kesalahan
    else:
        form = CoffeesForm()
    
    return render(request, 'coffees/add_coffees.html', {'form': form})



# UPDATE Game
def update_coffee(request, coffee_id):
    coffee = get_object_or_404(Menu, id=coffee_id)
    
    if request.method == 'POST':
        form = CoffeesForm(request.POST, request.FILES, instance=coffee)  # Tambahkan request.FILES untuk mengupload gambar
        if form.is_valid():
            form.save()  # Simpan perubahan ke database
            messages.success(request, 'Data coffee berhasil diubah!')
            return redirect('CoffeeList')  # Redirect ke halaman index game
    else:
        form = CoffeesForm(instance=coffee)  # Mengisi form dengan data game yang ada
    
    return render(request, 'coffees/update_coffees.html', {'form': form, 'menus': coffee})

# DELETE Game
def coffee_delete(request, coffee_id):
    if request.method == 'POST':
        coffee = get_object_or_404(Menu, id=coffee_id)
        coffee.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)