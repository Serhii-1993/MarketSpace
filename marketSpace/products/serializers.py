from rest_framework import serializers
from .models import Product, Image
from comments.serializers import CommentsSerializer


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


