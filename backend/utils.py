from .models import Shape, Triangle, Rectangle, Square, Diamond
from .v1.serializers import TriangleSerializer, RectangleSerializer, SquareSerializer, DiamondSerializer


def get_model_from_shape_type(shape_type):
    shape_type_mapping = {
        Shape.TRIANGLE: Triangle,
        Shape.RECTANGLE: Rectangle,
        Shape.SQUARE: Square,
        Shape.DIAMOND: Diamond,
    }
    return shape_type_mapping.get(shape_type, None)


def get_serializer_from_model(model):
    serializer_mapping = {
        Triangle: TriangleSerializer,
        Rectangle: RectangleSerializer,
        Square: SquareSerializer,
        Diamond: DiamondSerializer,
    }
    return serializer_mapping.get(model)


def get_choice_from_model(model):
    choices_mapping = {
        Triangle: Shape.TRIANGLE,
        Rectangle: Shape.RECTANGLE,
        Square: Shape.SQUARE,
        Diamond: Shape.DIAMOND,
    }
    return choices_mapping.get(model)
