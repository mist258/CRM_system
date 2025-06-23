from django.urls import path

from .views import CommentOrderCreateView

urlpatterns = [
    path('/<int:pk>/comments', CommentOrderCreateView.as_view(), name='comment'),

]
