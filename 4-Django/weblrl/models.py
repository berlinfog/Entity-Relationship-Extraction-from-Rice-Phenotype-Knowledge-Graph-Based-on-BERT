from django.db import models

# Create your models here.
class Usermsg(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    name=models.CharField(max_length=50,unique=True)
    passwd = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
class relation(models.Model):
    name=models.CharField(max_length=50)
    sentence=models.CharField(max_length=256)
    entity1=models.CharField(max_length=50)
    entity2=models.CharField(max_length=50)
    result=models.CharField(max_length=50,null=True)
class entity(models.Model):
     name=models.CharField(max_length=50)
     entity=models.CharField(max_length=50)
     friend=models.CharField(max_length=256,null=True)

class question(models.Model):
     name=models.CharField(max_length=50)
     question=models.CharField(max_length=256)
     answer=models.CharField(max_length=256)

