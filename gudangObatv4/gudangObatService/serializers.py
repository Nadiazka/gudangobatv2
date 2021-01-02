from rest_framework import serializers
from django.core.serializers import serialize
from django.contrib.auth.models import User, Group
from .models import *

class DrugsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Drugs
		fields = '__all__'

class PkmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Puskesmas
		fields = '__all__'

class DQSerializer(serializers.ModelSerializer):
	class Meta:
		model = DrugsQuantity
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]