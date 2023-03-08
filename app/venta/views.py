from django.http      import JsonResponse
from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Producto
from django.core      import serializers

""" 
    Servimos a paginas .html para las vistas
"""
def inicio( request ):
    return render(request, 'paginas/home.html')

def producto( request ):
    return render(request, 'paginas/productos.html')

def nuevo_producto( request ):
    return render(request, 'paginas/producto-crear.html')

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

    return JsonResponse({ 'status': 200, 'msg': "Producto eliminado correctamente!" })

