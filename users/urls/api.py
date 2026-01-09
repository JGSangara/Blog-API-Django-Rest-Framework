from django.urls import path

from ..views.api import CustomUserCreate, LoginView

app_name = "users_api"

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
