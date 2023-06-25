from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import EmotionalState
from .serializers import EmotionalStateSerializer


class EmotionalStateViewSet(ModelViewSet):
    queryset = EmotionalState.objects.all()
    serializer_class = EmotionalStateSerializer


def debugger(request):
    return render(request, 'debugger.html')
