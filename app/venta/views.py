from django.http      import JsonResponse
from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Producto
from django.core      import serializers
from .forms           import ProductoForm

""" 
    Servimos a paginas .html para las vistas
"""
def inicio( request ):
    return render(request, 'paginas/home.html')

def producto( request ):
    productos = Producto.objects.all()
    return render(request, 'paginas/productos.html', { 'productos': productos })

def nuevo_producto( request ):

    formulario = ProductoForm( request.POST or None )
    
    return render(request, 'paginas/producto-crear.html', { "form": formulario })

def crear_producto( request ):
    productos = Producto.objects.all()
    return render(request, 'paginas/productos.html', { 'productos': productos })

""" 
    Peticiones http para manejar con ajax
    en las vistas.
"""
def get_productos( request ):

    productos = list( Producto.objects.all() )

    if ( not ( len( productos ) > 0 ) ):
        data = { 'message': "No hay data!" }
        return JsonResponse( data )

    data = serializers.serialize('json', productos)

    return HttpResponse( data, content_type="application/json" )

def delete_producto( request, id_producto ):
    
    producto_found = Producto.objects.get( id_producto = id_producto )
    producto_found.delete()

    producto(request)


