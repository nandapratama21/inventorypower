import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from .models import Item
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    last_object = Item.objects.last()
    last_object = last_object.id
    # items = Item.objects.all()
    # Menghitung jumlah item yang ditambahkan
    username = request.user.username
    jumlah_item = Item.objects.filter(user=request.user).count()

    context = {
        'name': 'Muhammad Nanda Pratama',
        'class': 'PBP C',
        'items': items,
        'last_object' : last_object,
        'jumlah_item': jumlah_item,
        'username' : username,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)


def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request,id):
    deleted_item = Item.objects.get(pk=id) # ambil objeknya
    form = ItemForm(request.POST or None, instance=deleted_item)
    deleted_item.delete() # hapus objeknya
    return HttpResponseRedirect(reverse('main:show_main'))




def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response



def increment_amount(request, id):
    updated_item = Item.objects.get(pk=id)  # Ambil objeknya
    updated_item.amount += 1 # increment 1
    updated_item.save() # simpan nilainya
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_amount(request,id):
    updated_item = Item.objects.get(pk=id) # ambil objeknya
    updated_item.amount -= 1 # decrement 1
    updated_item.save() # simpan nilainya
    
    return HttpResponseRedirect(reverse('main:show_main'))



def item_id_last(request):
    last_object = Item.objects.last()
    return render(reverse('main:show_main'), {'last_object': last_object})

def get_item_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        # nilai awal amountnya adalah 1
        amount = 1
        user = request.user

        new_product = Item(name=name, amount=amount, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def delete_item_ajax(request,id):
    if request.method == 'POST':
        try:
            item_to_delete = Item.objects.get(pk=id)  # Cari item berdasarkan ID
            item_to_delete.delete()  # Hapus item
            return HttpResponse(b"DELETED", status=204)  # Respons dengan status 204 (No Content) menandakan penghapusan sukses
        except Item.DoesNotExist:
            return HttpResponseNotFound("Item not found")
    
    return HttpResponseNotFound()

