from core.view_imports import *  # isort: skip
from ..parameters import *  # isort: skip
from .serializers import *  # isort: skip

from django.core.exceptions import ObjectDoesNotExist

from ..models import Shape
from ..utils import get_model_from_shape_type, get_serializer_from_model
from .serializers import *


CUR_VERSION = 'v1'


class ListShapeByTypeView(APIView):

    @extend_schema(description='List Shapes by Type', responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    def get(self, request, shape_type=None):
        if shape_model := get_model_from_shape_type(shape_type):
            shape_model_serializer = get_serializer_from_model(shape_model)
            queryset = shape_model.objects.all()
            serializer = shape_model_serializer(queryset, many=True)
            return api_response_200(serializer.data)
        else:
            return api_response_400('Shape Type not found.')


class ReadDeleteShapeView(APIView):

    @extend_schema(description='Retrieve Shape by ID', responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def get(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            instance = shape_model.objects.get(id=shape_id)
            shape_model_serializer = get_serializer_from_model(shape_model)
            serializer = shape_model_serializer(instance)
            return api_response_200(serializer.data)
        except ObjectDoesNotExist:
            return api_response_400('Shape not found.')

    @extend_schema(description='Remove Shape by ID', responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def delete(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_instance.delete()
            return api_response_204()
        except ObjectDoesNotExist:
            return api_response_400('Shape not found.')


class PostUpdateShapeView(APIView):

    @extend_schema(description='Create a Shape', request=ShapeTypeSerializer, responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def post(self, request):
        for serializer in [TriangleSerializer, RectangleSerializer, SquareSerializer, DiamondSerializer]:
            shape_serializer = serializer(data=request.data)
            if shape_serializer.is_valid():
                shape_serializer.save()
                return api_response_200(shape_serializer.data)
        return api_response_400('Data inputed is NOT correct.')

    @extend_schema(description='Update a Shape', request=ShapeIDSerializer, responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def put(self, request):
        try:
            data = request.data
            shape_id = data['shape_id']
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            shape_model_serializer = get_serializer_from_model(shape_model)
            data['shape_type'] = shape_instance.shape_type
            instance = shape_model.objects.get(id=shape_id)
            serializer = shape_model_serializer(instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return api_response_200(serializer.data)
            return api_response_400('Data inputed is NOT correct.')
        except ObjectDoesNotExist:
            return api_response_400('Shape not found.')

    @extend_schema(description='Update a Shape', request=ShapeIDSerializer, responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def patch(self, request):
        try:
            data = request.data
            shape_id = data['shape_id']
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            shape_model_serializer = get_serializer_from_model(shape_model)
            data['shape_type'] = shape_instance.shape_type
            instance = shape_model.objects.get(id=shape_id)
            serializer = shape_model_serializer(instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return api_response_200(serializer.data)
            return api_response_400('Data inputed is NOT correct.')
        except ObjectDoesNotExist:
            return api_response_400('Shape not found.')


class CalculateShapeAreaPerimeterView(APIView):

    @extend_schema(description='Shape calculations by ID', responses={200: str}, tags=['Shape'])
    @check_allowed_versions(version=CUR_VERSION)
    @authentication_required()
    def get(self, request, shape_id=None):
        try:
            shape_instance = Shape.objects.get(id=shape_id)
            shape_model = get_model_from_shape_type(shape_instance.shape_type)
            instance = shape_model.objects.get(id=shape_id)
            serializer = ShapeAreaPerimeterSerializer(instance)
            return api_response_200(serializer.data)
        except ObjectDoesNotExist:
            return api_response_400('Shape not found.')
