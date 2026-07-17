from .models import Category, Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["name", "current_balance"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name",]