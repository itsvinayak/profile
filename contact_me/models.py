from django.db import models

class msg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    text=models.TextField()

    def __str__(self):
        return self.name
