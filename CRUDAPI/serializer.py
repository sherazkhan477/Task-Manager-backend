from rest_framework import serializers
from .models import TMSys,Users

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=TMSys
        fields=('__all__')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('UserId,UserName,UserEmail,Task')        