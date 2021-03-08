from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=25,null=False)
    note=models.TextField()
    created=models.DateTimeField(auto_now=True)
    archived=models.BooleanField(default=False)

    def __str__(self):
        return self.title