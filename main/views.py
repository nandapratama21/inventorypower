from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from .models import Item
from django.urls import reverse
from django.shortcuts import render

def show_main(request):
    items = Item.objects.all()
    # Menghitung jumlah item yang ditambahkan
    jumlah_item = Item.objects.count()
    context = {
        'name': 'Muhammad Nanda Pratama',
        'class': 'PBP C',
        'items': items,
        'jumlah_item': jumlah_item
    }

    return render(request, "main.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)


    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

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