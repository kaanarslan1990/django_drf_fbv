from django.db.models import fields
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    todo_detail = serializers.HyperlinkedIdentityField(view_name='todo-detail')

    class Meta:
        model = Todo
        fields = (
            'id',
            'task',
            'description',
            'priority',
            'done',
            'todo_detail'
        )
