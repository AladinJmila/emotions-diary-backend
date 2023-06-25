from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import EmotionalState
from .serializers import EmotionalStateSerializer


class EmotionalStateListView(ListAPIView):
    queryset = EmotionalState.objects.all()
    serializer_class = EmotionalStateSerializer


def debugger(request):
    return render(request, 'debugger.html')
