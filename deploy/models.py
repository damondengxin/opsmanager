from django.db import models

# Create your models here.

class Deploy(models.Model):
    project=models.CharField('项目名',max_length=100)
    address=models.CharField('项目地址',max_length=100,blank=True)
    curentversion=models.CharField('当前版本',max_length=100)
    deployhost=models.CharField('部署机器',max_length=50)
    hostip=models.CharField('ip',max_length=100)
    status = models.IntegerField('状态', choices=((0, '禁用'), (1, '启用')))
    create_timestamp = models.DateTimeField('创建时间', auto_now_add=True)
    last_update_timestamp = models.DateTimeField('最后更新时间', auto_now=True)

    def __str__(self):
        return self.project
