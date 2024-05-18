from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'vendor', 'platform', 'cost', 'renewal_date', 'account_info']
        labels = {
            'name': '服务名称',
            'vendor': '供应商',
            'platform': '平台',
            'cost': '费用',
            'renewal_date': '续订日期',
            'account_info': '账号信息'
        }
        help_texts = {
            'name': '请输入服务的名称',
            'vendor': '请输入供应商名称',
            'platform': '请输入平台名称',
            'cost': '请输入费用',
            'renewal_date': '请输入续订日期',
            'account_info': '请输入账号信息'
        }
