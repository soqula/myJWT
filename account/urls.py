from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from accounts.views import MyLoginView,MyLogoutView

app_name = "account"
urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]