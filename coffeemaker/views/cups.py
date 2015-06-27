from ..models import Cup

from rest_framework import viewsets
from ..serializers import CupSerializer

# ViewSets define the view behavior.


class CupViewSet(viewsets.ModelViewSet):
    queryset = Cup.objects.all()
    serializer_class = CupSerializer
