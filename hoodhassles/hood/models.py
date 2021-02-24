from django.db import models
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User

class Complain(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False)
    content = models.CharField(max_length=640, null=False)
    votes = models.IntegerField(default = 0)
    date = models.DateTimeField()
    ran = models.CharField(null=False, max_length=20)
    image = models.ImageField(upload_to='images/', blank=True)
    lati = models.DecimalField(max_digits=8, decimal_places=6)
    longi = models.DecimalField(max_digits=9, decimal_places=6)
    solved = models.BooleanField(null=False, default=False)
    voters = models.ManyToManyField(User, blank=True, related_name="voters")

'''
class Vote(models.Model):
    cid = models.ForeignKey(Complain, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
'''
