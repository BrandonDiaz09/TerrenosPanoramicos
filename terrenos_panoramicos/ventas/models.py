from django.db import models
from django.contrib.auth.models import User

class Inmueble(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    surface= models.DecimalField(max_digits=19, decimal_places=10)
    front = models.DecimalField(max_digits=15, decimal_places=10)
    bottom = models.DecimalField(max_digits=15, decimal_places=10)

    photo = models.ImageField(upload_to='ventas/photos_terrenos')

    creted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return '{} by @{}'.format(self.surface, self.user.username)