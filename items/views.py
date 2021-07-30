from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Recipes



def recipe_list(request):
    recipe=Recipes.objects.all()
    return render(request, 'items/list.html', {'recipe': recipe})

def create(request):
    return render(request, 'items/create.html')

def data(request):
    if request.method == "POST":
        Recipes.objects.create(
            name=request.POST["name"],
            ingredients = request.POST["ingredients"],
            process=request.POST["process"],
            image=request.FILES["image"])
        return HttpResponseRedirect('/items/recipe_list/')
    return render (request, 'items/create.html')

def details(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'items/details.html', {'recipe':recipe})
