from dataclasses import field
from rest_framework import serializers
from butce.models import Transaction


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'