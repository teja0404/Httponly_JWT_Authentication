from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from .views import ObtainTokenPairWithColorView, CustomUserCreate


urlpatterns = [
    path('',views.home),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

