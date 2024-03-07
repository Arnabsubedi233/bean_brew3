from django.db import models

# Create your models here.
class reservation(models.Model):

    CITY =[
        ('Harrogate','Harrogate'),
        ('Leeds','Leeds'),
        ('Knaresborough Castle','Knaresborough')
    ]
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.IntegerField()
    restaurant = models.CharField(max_length = 100,choices=CITY)
    number_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(null=True,blank = True)
    

    def __str__(self):
        return self.name