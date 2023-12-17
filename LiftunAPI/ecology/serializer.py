from rest_framework import serializers

from ecology.models import Ecology


class EcologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecology
        fields = '__all__'
