from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    status = models.BinaryField(default=True)

    class Meta:
        abstract = True


class Service(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.title



