import datetime

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from home.api.v1.serializers import SignupSerializer, UserSerializer, UserTaskSerializer
from home.models import Task
from users.forms import User


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ["post"]

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user, context={"request": request})
            return Response({"token": token.key, "user": user_serializer.data})
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserTaskViewSet(ModelViewSet):
    serializer_class = UserTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = datetime.date.today()
        # today = '2023-03-21'
        is_complete = self.request.query_params.get("is_complete")
        date = self.request.query_params.get("date")
        queryset = Task.objects.filter(user=self.request.user)
        if is_complete:
            queryset = queryset.filter(is_complete=is_complete)
        if date:
            queryset = queryset.filter(task_date_time__date=date)
        else:
            queryset = queryset.filter(task_date_time__date__gte=today)
        return queryset.order_by("task_date_time")


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset
