from django.db import models

class Blog(models.Model):
    message = models.CharField(max_length=200)
    update_time = models.DateField(auto_now=True)