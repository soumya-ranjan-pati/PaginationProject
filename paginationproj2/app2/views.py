from django.shortcuts import render,redirect
from app2.models import ProductModel
from django.core.paginator import Paginator

# Create your views here.
def show(request):
    return render(request,"index.html")


def add_product(request):
    id=request.POST.get("t1")
    pho=request.FILES['t2']
    ProductModel(idno=id,photo=pho).save()
    return redirect('save_product')


def save_product(request):
    result=ProductModel.objects.all()
    pa=Paginator(result,3)
    page_number=request.GET.get("page_no",1)
    page=pa.page(page_number)
    return render(request,"save_product.html",{"data":page})