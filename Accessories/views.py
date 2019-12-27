from django.shortcuts import render
from django.http import HttpResponse
from Accessories.models import ProductTree
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"main.html")
def add(request,name,parent_id):
    p = ProductTree(name = name,parent_id=parent_id)
    p.save()
    return HttpResponse("Hello added")
def view(request,parent_id):
    ps = ProductTree.objects.filter(parent_id=parent_id)
    jsonout = {parent_id:[{"name":p.name,"id":p.id} for p in ps]}
    return JsonResponse(jsonout)
