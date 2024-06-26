from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True)

    # ССЫЛКИ НА СОЦ СЕТИ
    github_link = models.URLField(null=True, blank=True)
    figma_link = models.URLField(null=True, blank=True)
    vk_link = models.URLField(null=True, blank=True)
    tg_link = models.URLField(null=True, blank=True)
    cloud_link = models.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





