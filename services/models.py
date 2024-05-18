from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='服务名称')
    vendor = models.CharField(max_length=64, verbose_name='供应商')
    platform = models.CharField(max_length=64, verbose_name='平台')
    cost = models.FloatField(verbose_name='费用')
    renewal_date = models.DateField(verbose_name='续订日期')
    account_info = models.CharField(max_length=128, verbose_name='账号信息')

    def __str__(self):
        return self.name
