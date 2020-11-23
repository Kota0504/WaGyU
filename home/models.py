from django.db import models

class PartsModel(models.Model):
    parts_name = models.CharField(max_length=50)
    template = models.CharField(max_length=50)

    def __str__(self):
        return self.parts_name
