from django.db import models
import shortuuid
def tns():
    s = shortuuid.ShortUUID(alphabet="0123456789uabcdefghijklmnopqrstvwxyz")
    otp = s.random(length=15)
    return otp

# Create your models here.
class Googlerecharge(models.Model):
    email = models.EmailField(null=False,blank=False)
    transid = models.CharField(max_length=15,unique=True,default=tns)
    googleid = models.CharField(max_length=15,unique=True,null=True,blank=True)
    amount = models.BigIntegerField(null=False,blank=False,default=0)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return self.email