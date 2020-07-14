from django.urls import path,re_path, include
from rest_framework_simplejwt import views as jwt_views
from .views import (ObtainTokenPairWithColorView,
                    CustomUserCreate, HelloWorldView,
                    LogoutAndBlacklistRefreshTokenForUserView)
from rest_framework import routers
from api.views import QuestionViewSet
from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'signup', SignUpViewset, basename='sign-up')
router.register(r'forfait', ForfaitViewset, basename='forfait')

urlpatterns = [
    path(r'user/', include(router.urls)),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(),
         name='blacklist')
]

