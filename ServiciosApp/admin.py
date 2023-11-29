from django.contrib import admin
from .models import Servicio

# Register your models here.

# Esta clase la creamos para que el panel de admin nos permita ver el created y updated, al menos, en modo solo lectura.
class ServicioAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')


# Agregamos el registro de nuestro servicio al panel de admin, pasandole el servicio, 
# y tambien la clase anterior para ver los solo lectura.
admin.site.register(Servicio, ServicioAdmin)