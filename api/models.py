from django.db import models

# Create your models here.


class Employees(models.Model):
    fullName = models.CharField(null=False, blank=False,  max_length=50)
    position = models.CharField(null=False, blank=False,  max_length=50)
    office = models.CharField(null=False, blank=False,  max_length=50)
    salary = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName[0:50]

    class Meta:
        ordering = ['-updated']