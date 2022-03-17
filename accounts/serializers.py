from rest_framework import serializers
from accounts.models import ProfileModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileModel
        fields=["username","password","email","credit","Gender","ProfileImage"]

 