from django.urls import include, path

from . import views


urlpatterns = [
    path('debugger', views.debugger),
    path('emotional-states/', views.EmotionalStateListView.as_view(),
         name='emotional-state-list')
]
