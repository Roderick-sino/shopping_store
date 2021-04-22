from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """自定义用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        db_table = 'tb_users'  # 自定义表名
        verbose_name = '用户'  # 单数形式
        verbose_name_plural = verbose_name  # 复数形式

    def __str__(self):  # 调试程序
        return self.username
