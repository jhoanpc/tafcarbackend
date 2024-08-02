from . import models

from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        
        fields = ('fullname',
                'typedoc',
                'nroDoc',
                'gender',)
        read_only_fields = ('created_at',)


class DetailsPersonSerializer(serializers.ModelSerializer):        
    class Meta:
        model = models.DetailsPerson
        fields = '__all__'

class DetailsEconomicActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetailsEconomicActivity
        fields = '__all__'
         
        