from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Treasure, File_Treasure, Site_Style, Treasure_Ultra
from .forms import TreasureForm, File_TreasureForm, Site_StyleForm, Treasure_UltraForm
from django.contrib.auth.forms import UserCreationForm
import operator
from django.db.models import Q

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def ultra_treasure_detail(request, pk):
    ultra_treasure = Treasure_Ultra.objects.get(id=pk)
    return render(request, 'shelf/ultra_treasure_detail.html', {'ultra_treasure': ultra_treasure})

def ultra_treasure_list(request):
    ultra_treasures = Treasure_Ultra.objects.all()
    return render(request, 'shelf/ultra_treasure_list.html', {'ultra_treasures': ultra_treasures})

def ultra_treasure_create(request):
    if request.method == 'POST':
         form = Treasure_UltraForm(request.POST, request.FILES)
         if form.is_valid():
            ultra_treasure = form.save()
            return redirect('ultra_treasure_detail', pk=ultra_treasure.pk)
    else:
        form = Treasure_UltraForm()
    return render(request, 'shelf/ultra_treasure_form.html', {'form': form})


def ultra_treasure_edit(request, pk):
    ultra_treasure = Treasure_Ultra.objects.get(pk=pk)
    if request.method == "POST":
        form = Treasure_UltraForm(request.POST, request.FILES, instance=ultra_treasure)
        if form.is_valid():
            ultra_treasure = form.save()
            return redirect('ultra_treasure_detail', pk=ultra_treasure.pk)
    else:
        form = Treasure_UltraForm(instance=ultra_treasure)
    return render(request, 'shelf/ultra_treasure_form.html', {'form': form})


def ultra_treasure_delete(request, pk):
    Treasure_Ultra.objects.get(id=pk).delete()
    return redirect('ultra_treasure_list')

def about_ultra_treasure_list(request):
    return render(request, 'shelf/about_ultra_treasure_list.html')

