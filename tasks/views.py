from rest_framework import generics, permissions
from django_q.tasks import async_task
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer
from django.contrib.auth import get_user_model
from .tasks import send_email_notification

class RegisterUser(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class SmartTaskRankView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user, completed=False).order_by('due_date', '-priority')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class SendEmailView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        recipient_list = request.data.get('recipient_list', [])

        async_task('tasks.tasks.send_email_notification', subject, message, recipient_list)
    
        return Response({"message": "Email task has been triggered!"})