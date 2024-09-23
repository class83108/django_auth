from allauth.account.utils import perform_login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages


from .forms import MyUserCreationForm, AlluthUserProfileForm


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


@login_required
def auth_success(request):
    form = MyUserCreationForm(instance=request.user)
    user = request.user

    if user.socialaccount_set.exists():
        # 先確認是否已經註冊過了
        if user.is_staff and user.phone:
            messages.success(request, "歡迎回來！")
            # 不需要登入，直接導向首頁 因為裝飾器有login_required
            return redirect("admin:index")

        # 如果還不是staff 將其設定為staff
        if not user.is_staff:
            user.is_staff = True
            user.save()

        # 如果沒有填寫 phone 資料，則導向填寫 phone 資料的頁面
        if not user.phone:
            if request.method == "POST":
                form = AlluthUserProfileForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    messages.success(request, "感謝你完善個人資料！")
                    return redirect("admin:index")
            else:
                form = AlluthUserProfileForm(instance=user)
            return render(request, "complete_profile.html", {"form": form})
        else:
            login(request, user)
            messages.success(request, "歡迎回來！")
            return redirect("admin:index")

    else:
        return redirect(reverse("user:register"))
