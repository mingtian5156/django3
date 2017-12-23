from django.db import models

class OrderInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo')
    oid = models.CharField(max_length=20,primary_key=True)
    odate = models.DateTimeField(auto_now=True)
    oIsPay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=8,decimal_places=2)
    oaddress = models.CharField(max_length=150)
    def __str__(self):
        return self.oid


# wufu shixian zhenshizhifu wuliuxinxi 
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    count = models.IntegerField()
   