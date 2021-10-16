from rest_framework import serializers
from . models import User

class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['userId', 'name', 'username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def save(self):
    #     def username_exists(username):
    #         if User.objects.filter(username=username).exists():
    #             return True
    #
    #         return False
    #
    #     user = User(
    #             userId=self.validated_data['userId'],
    #             name=self.validated_data['name'],
    #             password=self.validated_data['password'],
    #         )
    #     username = self.validated_data['username']
    #
    #     if username_exists(username):
    #         raise serializers.ValidationError({'username': 'username already exists'})
    #     user.set_username(username)
    #     user.save()
    #     return user


# class LoginSerializer(serializers.ModelSerializer):
#     model = User
#     fields = ['username', 'password']
#
#     extra_kwargs = {
#         'password': {'write_only': True}
#     }

class DeleteAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']
