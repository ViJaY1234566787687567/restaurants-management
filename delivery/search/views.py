from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def search(request):
    products=None
    query=""
    if(request.method=="POST"):
        query=request.POST['q']
        print("quest",query)
        if query:

            products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'search.html',{'query':query,'p':products})
