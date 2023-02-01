from django.db import models

# Create your models here.
class Img(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,default='/holder.jpeg')

    def __str__(self) -> str:
        return self.title + " " + self.desc