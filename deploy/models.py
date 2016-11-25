from django.db import models

# Create your models here.

class Deploy(models.Model):
    project=models.CharField('项目名',max_length=100)
    address=models.CharField('项目地址',max_length=100,blank=True)
    curentversion=models.CharField('当前版本',max_length=100)
    deployhost=models.CharField('部署机器',max_length=50)
    hostip=models.IntegerField('ip')
    action=models.CharField('动作',max_length=100)

    def __str__(self):
        return self.project