from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="sign_up"),
    # path('reset_password/', views.ResetPasswordView.as_view(), name="reset_password")
]
