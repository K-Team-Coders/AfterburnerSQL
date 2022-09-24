from django.db import models

class TableUsabilityOperators(models.Model):
    _name = models.CharField(default=' ', max_length=50)
    _from = models.IntegerField(default=1)
    _into = models.IntegerField(default=1)
    _join = models.IntegerField(default=1)
