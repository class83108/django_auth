from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        # 這裡加上我們自定義的 phone 欄位
        fields = UserCreationForm.Meta.fields + ("phone",)
