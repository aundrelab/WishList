from rest_framework import serializers
from . models import User

class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['userId', 'name', 'username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }
