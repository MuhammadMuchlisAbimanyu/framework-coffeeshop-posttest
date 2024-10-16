from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now
import os

def coffee_image_upload_path(instance, filename):
    # Ambil ekstensi file asli (contoh: '.jpg', '.png')
    ext = filename.split('.')[-1]
    # Buat nama file baru berdasarkan judul game dan waktu saat ini
    filename = f"{instance.name}_{now().strftime('%Y%m%d%H%M%S')}.{ext}"
    # Simpan di folder 'games_images/'
    return os.path.join('coffee_images/', filename)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0.01)  # Harga minimal adalah 0.01
    ])
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to=coffee_image_upload_path, default='coffees_images/default.jpg')

    def __str__(self):
        return self.name
