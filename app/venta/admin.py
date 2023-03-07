from django.contrib import admin
from .models import Venta
from .models import Detalle
from .models import Usuario
from .models import Producto

# Register your models here.
admin.site.register( Venta )
admin.site.register( Detalle )
admin.site.register( Usuario )
admin.site.register( Producto )
