from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categorias'
    
    def _str_(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=5000, default='')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)  # Por ejemplo, el valor predeterminado se establece en 0
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    precio_anterior = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) #Solo aplica a la categoria OFERTAS

    class Meta:
        verbose_name_plural = 'productos'
    
    def _str_(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tienda/images')

    def _str_(self):
        return f'Imagen para {self.producto.nombre}'