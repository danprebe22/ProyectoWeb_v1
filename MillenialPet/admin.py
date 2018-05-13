from django.contrib import admin
from .models import Cliente
from .models import Cita
from .models import Producto
from .models import Lista
from .models import Lista_cliente
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cita)
admin.site.register(Producto)
admin.site.register(Lista_cliente)
admin.site.register(Lista)


