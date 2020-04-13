
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from api.views import QuestionViewSet
from rest_framework import routers
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', api_views.home, name='api-home'),
    path('api/', include('authentication.urls')),
    path('q/', include('frontend.urls'))
]
