from rest_framework import serializers
from apps.blog.models import Cars


class CarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars
        fields = ('id', "title", "content", "photo", "cat", "user")
