from django.urls import path
from .views import RegisterUser, TaskListCreateView, TaskRetrieveUpdateDestroyView, SmartTaskRankView, SendEmailView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('tasks/smart-rank/', SmartTaskRankView.as_view(), name='task-rank'),
    path('send-email/', SendEmailView.as_view(), name='send-email'),
]
