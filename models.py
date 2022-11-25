from django.db import models


class document(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.CharField(max_length=1200)

class apiData(models.Model):
    cpn = models.BigIntegerField(unique=True)
    cpd = models.CharField(max_length=1500, blank=True, default=None)
    irn = models.PositiveIntegerField(default=None)
    qp = models.FloatField(default=None)



# Create your models here.
