from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from users.views import CustomUserRegisterViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'register', CustomUserRegisterViewSet, basename='register')
router.register(r'user', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
