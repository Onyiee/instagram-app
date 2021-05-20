from django.db import models


# Create your models here.
class photo(models.Model):
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo
