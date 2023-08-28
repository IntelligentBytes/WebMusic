from django.db import models
from datetime import timedelta

# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='musics/')
    duration = models.DurationField()
    publish_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'

