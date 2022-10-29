from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0, null=True)
    sex = models.IntegerField(default=0, null=True)  # 0 = girl 1 = male
    email = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'Yuuzu_User'

class Payment(models.Model):
    payId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    isPay = models.BooleanField(default=False)

    class Meta:
        db_table = 'Yuuzu_Payment'
