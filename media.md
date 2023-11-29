# Archivos Multimedia en Django
Por defecto, Django no sabe administrar, y por ende mostrar, archivos multimedia. Para eso, debemos configurar:
1. Donde los almacenará
2. De donde los extraerá (donde buscarlos)

## Configuracion de URL media
Para ello debemos crear en el directorio del proyecto una carpeta `media`, y luego modificar nuestro `settings.py` y agregar la direccion de esa carpeta para que sea administrada.
```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
## Direccion en el models
Ahora bien, si bien ya podrá mostrar las imagenes, debemos en nuestro Model asignar donde las guardará. Esto es debido a que, podemos tener imágenes, videos y audios, provenientes de cáda uno de las apps que agreguemos, y para poner orden los organiremos. Esto se logra agregando al Model la direccion donde guardará la imagen.
```
class Servicio (models.Model):
	...
	imagen = models.ImageField(upload_to = 'servicios/imagenes')
	...
```
Con esto, nos creará el directorio `media/servicios/imagenes` y ahi almacenará las imagenes de este model.

## Asignando URL media a Path
Lo siguiente es asignar esta direccion en el **path del proyecto** (`urls.py`) para poder visualizarlo, sino nos arroja un error 404
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```