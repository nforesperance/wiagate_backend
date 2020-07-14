
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from api.views import QuestionViewSet, QuizViewSet
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'app/questions', QuestionViewSet, basename='questions')
router.register(r'app/quiz', QuizViewSet, basename='quiz')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', api_views.home, name='api-home'),
    path('api/', include('authentication.urls')),
    path('q/', include('frontend.urls'))
]

urlpatterns += router.urls
