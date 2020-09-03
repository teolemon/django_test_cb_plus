from django.shortcuts import get_object_or_404, render
from django.template import loader

from .forms import ItemForm

from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Inventory
import requests
import re

#from rest_framework.views import APIVirw 


# Create your views here.

def index(request):
    latest_inventory_list = Inventory.objects.order_by('expiry_date')
    template = loader.get_template('inventory/index.html')
    context = {
        'latest_inventory_list': latest_inventory_list,
    }
    return HttpResponse(template.render(context, request))

def item_create(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        
        data_json = api_world_food(item.gtin)
        item.name = extract_name(data_json)
        item.url_photo = extract_url_image(data_json)

        for i in Inventory.objects.all():
            if i.gtin == item.gtin:
                i.expiry_date = item.expiry_date
                i.save()
                return HttpResponseRedirect(reverse('index'))
        item.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "inventory/add.html", {'form': form})

def delete_item(request, pk): 
    Inventory.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('index'))

def modify_item(request, pk):
    item = Inventory.objects.get(id=pk)
    form = ItemForm(request.POST)
    if form.is_valid():
        itemF = form.save(commit=False)
        item.name = itemF.name
        item.expiry_date = itemF.expiry_date
        for i in Inventory.objects.all():
            if i.gtin == itemF.gtin:
                item.save()
                return HttpResponseRedirect(reverse('index'))
        item.gtin = itemF.gtin
        item.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form,
        'item': item
    }
    return render(request, "inventory/modify.html", context)


def detail(request, id):
    item = get_object_or_404(Inventory, pk=id)
    return render(request, 'inventory/detail.html', {'item': item})


def api_world_food(id):
    url = 'https://world.openfoodfacts.org/api/v0/product/'+str(id)+'.json'

    request = requests.get(url)
    data = request.json()

    return data

def extract_name(data):
    str1 = re.findall("\'product_name\': \'.*\',", str(data))
    str2 = str(str1).split(",")
    name = str(str2[0]).split(":")[1]
    return name

def extract_url_image(data):
    str1 = re.findall("\'image_small_url\': \'.*\',", str(data))
    str2 = str(str1).split(",")
    url = str(str2[0]).split(" ")[1]
    return url

