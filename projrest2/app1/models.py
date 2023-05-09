from django.db import models

# Create your models here.
class App(models.Model):

    created = models.DateTimeField()
    title = models.CharField(max_length=30)
    code = models.TextField()
    linenos = models.BooleanField()
    language = models.CharField(max_length=30)
    style = models.CharField(max_length=30)

    class Meta:
        ordering =  ['created']
