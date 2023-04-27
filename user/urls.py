from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from user.views import (
    ProfileViewSet,
    UserFollowersViewSet,
    CreateUserView,
    ManageUserView,
    LogoutView
)

router = routers.DefaultRouter()

router.register("profiles", ProfileViewSet)
router.register("followers", UserFollowersViewSet)


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
] + router.urls

app_name = "user"
