from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django_validated_jsonfield import ValidatedJsonModelSerializerMixin

from ..models import Triangle, Rectangle, Square, Diamond


class TriangleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Triangle
        fields = '__all__'


class RectangleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rectangle
        fields = '__all__'


class SquareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Square
        fields = '__all__'


class DiamondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diamond
        fields = '__all__'


class BaseShapeSerializer(serializers.Serializer):
    shape_type = serializers.CharField(label='Shape Type')
    side_a = serializers.FloatField(label='Side A', required=False)
    side_b = serializers.FloatField(label='Side B', required=False)
    side_c = serializers.FloatField(label='Side C', required=False)
    width = serializers.FloatField(label='Width', required=False)
    height = serializers.FloatField(label='Height', required=False)
    side = serializers.FloatField(label='Side', required=False)
    diagonal_1 = serializers.FloatField(label='Diagonal 1', required=False)
    diagonal_2 = serializers.FloatField(label='Diagonal 2', required=False)


class ShapeTypeSerializer(BaseShapeSerializer):
    shape_type = serializers.CharField(label='Shape Type')


class ShapeIDSerializer(BaseShapeSerializer):
    shape_id = serializers.IntegerField(label='Shape ID')


class ShapeAreaPerimeterSerializer(BaseShapeSerializer):
    area = serializers.FloatField()
    perimeter = serializers.FloatField()
