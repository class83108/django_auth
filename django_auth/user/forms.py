from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        # 這裡加上我們自定義的 phone 欄位
        fields = UserCreationForm.Meta.fields + ("phone",)


User = get_user_model()


class AlluthUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone"]
