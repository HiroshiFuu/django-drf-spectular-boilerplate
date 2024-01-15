
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter


SHAPE_TYPE_PATH_PARAMETER = OpenApiParameter('shape_type', OpenApiTypes.STR, OpenApiParameter.PATH, required=True, description='Shape Type')
SHAPE_ID_PATH_PARAMETER = OpenApiParameter('shape_id', OpenApiTypes.STR, OpenApiParameter.PATH, required=True, description='Shape ID')
