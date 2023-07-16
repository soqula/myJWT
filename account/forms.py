from django import forms
from django.forms.fields import DateField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm

from .models import User
from myjwt.models import Profile


class CustomAdminChangeForm(UserChangeForm):
#Profileクラスのフィールドを追記します
    username = forms.CharField(max_length=100)
    opt_disp_list = forms.IntegerField(required=False) 

    class Meta:
        model = User
        fields =('email', 'password', 'active', 'admin')

#Profileが存在する場合は、初期値にデータを格納する
    def __init__(self, *args, **kwargs):
        user_obj = kwargs["instance"]
        if hasattr(user_obj, "profile"):
            profile_obj = user_obj.profile
            self.base_fields["username"].initial = profile_obj.username
            self.base_fields["opt_disp_list"].initial = profile_obj.opt_disp_list
        super().__init__(*args, **kwargs)

#保存機能の定義
    def save(self, commit=True):
        user_obj = super().save(commit=False)
        username = self.cleaned_data.get("username")
        opt_disp_list = self.cleaned_data.get("opt_disp_list")
        if hasattr(user_obj, "profile"):
            profile_obj = user_obj.profile
        else:
            profile_obj = Profile(user=user_obj)
        if username is not None:
            profile_obj.username = username
        if opt_disp_list is not None:
            profile_obj.opt_disp_list = opt_disp_list
        profile_obj.save()
        if commit:
            user_obj.save()
        return user_obj

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

#以下を追記
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user_email = self.instance.user.email
        if username == user_email:
            raise forms.ValidationError("ユーザー名を変更してください")
        elif "@" in username:
            raise forms.ValidationError("ユーザー名にEメールアドレスは使用できません")
        return username