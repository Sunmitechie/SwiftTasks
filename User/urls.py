from django.urls import path
from .views import RegisterUser, LoginUser, AdminOnlyView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
]
