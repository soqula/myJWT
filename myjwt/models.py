from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Profile(models.Model):
    """ユーザプロファイル"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, verbose_name="ユーザー名")
    opt_disp_list = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class HistoryWeight(models.Model):
    """体重の履歴"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saved_at = models.DateField(verbose_name="記録日")
    weight = models.FloatField(verbose_name="体重", default=0)
