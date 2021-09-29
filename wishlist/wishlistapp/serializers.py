from rest_framework import serializers
from . models import User

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ('username', 'password')
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['']