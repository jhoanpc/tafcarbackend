
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework. parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView

# Create your views here.

@csrf_exempt

class PersonView (APIView):
    def get(self, request, format= None):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many= True)
        return JsonResponse(serializer.data, safe=False)   

