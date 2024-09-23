from django.urls import path
from .views import register_view, auth_success

urlpatterns = [
    path("auth-success/", auth_success, name="auth_success"),
    path("", register_view, name="register"),
]
