from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivationManagerView, SendActivationEmailView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/<str:token>/activate', ActivationManagerView.as_view(), name='auth_activate'),
    path('/<int:pk>/email', SendActivationEmailView.as_view(), name='auth_email'),

]