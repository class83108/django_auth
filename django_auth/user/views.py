from django.shortcuts import render

from .forms import MyUserCreationForm


def register_view(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        # print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            # 加入註冊成功的訊息
            msg = "註冊成功"

        else:
            msg = "註冊失敗"
    form = MyUserCreationForm()
    return render(request, "user/register.html", {"form": form})
