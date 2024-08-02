from .models import Person,DetailsEconomicActivity,DetailsPerson
from rest_framework import viewsets, permissions
from .serializers import PersonSerializer, DetailsEconomicActivitySerializer, DetailsPersonSerializer
from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = PersonSerializer
    
class DetailsEconomicActivityViewSet(viewsets.ModelViewSet):
    queryset= DetailsEconomicActivity.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = DetailsEconomicActivitySerializer

class DetailsPersonViewSet(viewsets.ModelViewSet):
    queryset=DetailsPerson.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = DetailsPersonSerializer