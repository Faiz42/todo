from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import SignupViewSet, LoginViewSet, UserTaskViewSet, UserProfileViewSet

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("profile", UserProfileViewSet, basename="profile")
router.register("user-task", UserTaskViewSet, basename="user_task")

urlpatterns = [
    path("", include(router.urls)),
    ]
