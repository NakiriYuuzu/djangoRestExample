from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0, null=True)
    sex = models.IntegerField(default=0, null=True)  # 0 = girl 1 = male
    email = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'Yuuzu_Test'
