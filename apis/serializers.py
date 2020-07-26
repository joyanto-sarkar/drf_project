from rest_framework import serializers
from todo import models

class TodoSerializer(serializers.ModelSerializer):
    """  serializes todo items """

    class Meta:
        model = models.Todo
        fields = ('id','title','description' , 'status')
