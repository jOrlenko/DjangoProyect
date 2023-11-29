from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = 'categoria'
		verbose_name_plural = 'categorias'

	def __str__(self):
		return self.nombre
		
# autor:
# hemos importado los users, para que puedan crear posts
# # pero con el 'on_delete' hemos configurado que todos sus post se borren al elimar el user
#categorias:
# relacion many to many (vario a varios)
# varios post de una categoria y/o varias categorias en un post

class Post (models.Model):
	titulo = models.CharField(max_length=50)
	detalle = models.CharField(max_length = 100)
	imagen = models.ImageField(upload_to= 'blog/imagenes', null=True, blank=True)
	contenido = models.CharField(max_length = 5000)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	categorias = models.ManyToManyField(Categoria)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'

	def __str__(self):
		return self.titulo