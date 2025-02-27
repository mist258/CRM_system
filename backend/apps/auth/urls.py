from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivationManagerView, RecoveryPasswordRequestView, SendActivationEmailView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivationManagerView.as_view(), name='activate_account'),
    path('/<int:pk>/email', SendActivationEmailView.as_view(), name='token_email'),
    path('/manager/recovery', RecoveryPasswordRequestView.as_view(), name='auth_recovery'),

]