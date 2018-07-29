from django.db import models

class Database(models.Model):
    first_name  = models.CharField(max_length=255, blank=True, default='')
    last_name     = models.CharField(max_length=255, blank=True, default='')
    phone       = models.CharField(max_length=14, blank=True, unique=True)
    email       = models.EmailField(unique=True)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
