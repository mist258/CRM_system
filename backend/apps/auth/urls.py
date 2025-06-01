from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ActivationManagerView,
    CrateActivationTokenForManagerView,
    RecoveryPasswordRequestView,
    RecoveryPasswordView,
    SendActivationEmailView,
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivationManagerView.as_view(), name='activate_account'),
    path('/<int:pk>/email', SendActivationEmailView.as_view(), name='token_email'),
    path('/manager/recovery_request', RecoveryPasswordRequestView.as_view(), name='auth_recovery'),
    path('/manager/change_password/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery'),
    path('/manager/<int:pk>/activation_token', CrateActivationTokenForManagerView.as_view(), name='create_token'),

]