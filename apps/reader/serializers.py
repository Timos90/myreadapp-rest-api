from rest_framework import serializers
from .models import Reader
from django.contrib.auth.models import User



class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude = ('password', )

class ReaderSerializer(serializers.ModelSerializer):
    user = UserSerilizer()
    class Meta:
        model = Reader
        fields = '__all__'
        #depth = 1
