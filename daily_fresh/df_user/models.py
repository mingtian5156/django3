from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    upostname = models.CharField(max_length=20,default='')
    uaddress = models.CharField(max_length=100,default='')
    upostcode = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')
    def __str__(self):
        return self.uname
#default,blank shi python cengmiande buyingxiang shuju biaojiegou