from django.shortcuts import render
from django.http      import HttpResponse

from .models          import Producto

# Create your views here.
def inicio( request ):
    return render(request, 'paginas/home.html')

def producto( request ):
    productos = Producto.objects.all()
    return render(request, 'paginas/productos.html', {'productos': productos })

def nuevo_producto( request ):
    return render(request, 'paginas/producto-crear.html')
