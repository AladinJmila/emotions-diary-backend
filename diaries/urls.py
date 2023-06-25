from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('emotional-states', views.EmotionalStateViewSet)

urlpatterns = [
    path('debugger', views.debugger),
    path('', include(router.urls))
]
