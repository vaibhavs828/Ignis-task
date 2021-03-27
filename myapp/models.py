from django.db import models

# Create your models here.
class Ignis(models.Model):
    event_name=models.CharField(max_length=50,blank=False)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=50)
    image=models.ImageField(upload_to='app/images',default="")
    is_liked=models.BooleanField(default=False)

    def __str__(self):
        return self.event_name
    
