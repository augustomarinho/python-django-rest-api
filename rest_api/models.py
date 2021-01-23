from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    document = models.CharField(max_length=10)
    birth = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Person'


class Training(models.Model):
    LEVEL = (
        ('B', 'BASIC'),
        ('I', 'INTERMEDIATE'),
        ('A', 'ADVANCED')
    )
    training_code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    class Meta:
        db_table = 'Training'
