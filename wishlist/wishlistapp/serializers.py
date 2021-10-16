from rest_framework import serializers
from . models import User

class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        def username_exists(username):
            if User.objects.filter(username=username).exists():
                return True

            return False

        user = User(
            name=self.validated_data['name'],
            password=self.validated_data['password'],
        )
        username = self.validated_data['username']

        if username_exists(username):
            raise serializers.ValidationError({'username': 'username already exists'})
        user.set_username(username)
        user.save()
        return user



class DeleteAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def check(self):
        if self.username_exists(self.validated_data['username']):
            user = User.objects.get(username=self.validated_data['username'])
            if user.password != self.validated_data['password']:
                raise serializers.ValidationError({'failure': 'incorrect password'})
                return False
        else:
            raise serializers.ValidationError({'failure': 'username does not exist'})
            return False

        return True

    def username_exists(self, username):
        if User.objects.filter(username=username).exists():
            return True

        return False

class LogoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }
