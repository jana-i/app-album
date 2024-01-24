from django.db import models

# Create your models here.

class Member(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    genre = models.CharField(max_length=40, default='Pop')
    cena = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title + " " + self.artist + " " + self.genre + " " + self.cena
