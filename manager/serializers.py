from rest_framework import serializers
from .models import *


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationType
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    type = OperationTypeSerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'type']


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']


class TransactionSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    type = OperationTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)

    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source='status',
        required=False,
        allow_null=True
    )
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=OperationType.objects.all(),
        source='type',
        required=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        required=True
    )
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(),
        source='subcategory',
        required=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id',
            'created_date',
            'status',
            'type',
            'category',
            'subcategory',
            'amount',
            'comment',
            # writable fields
            'status_id',
            'type_id',
            'category_id',
            'subcategory_id',
        ]
        read_only_fields = [
            'status',
            'type',
            'category',
            'subcategory',
        ]



