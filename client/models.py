from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=30)
    review = models.TextField(max_length=100)
    image = models.ImageField(upload_to="client/", blank=True, null=True)

    def __str__(self):
        return self.full_name
