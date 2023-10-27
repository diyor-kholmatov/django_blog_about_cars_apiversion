from rest_framework import serializers
from apps.blog.models import Cars, Payment


class CarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars
        fields = ('id', "title", "content", "photo", "cat", "user")


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

