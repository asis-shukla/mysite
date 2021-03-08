from rest_framework import serializers
from .models import Hero
from .models import Student

class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        feildsnow = ('name', 'alias', 'age'), 
        fields = '__all__'

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        feildsnow = ('name', 'grade', 'date_of_birth', 'percentage'), 
        fields = '__all__'
