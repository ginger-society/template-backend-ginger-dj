"""Views for the src app"""
from datetime import datetime

from ginger.drf_yasg import openapi
from ginger.drf_yasg.utils import swagger_auto_schema
from ginger.http import JsonResponse
from ginger.rest_framework import serializers
from ginger.rest_framework.decorators import api_view
from ginger.views.decorators.cache import cache_page
from prometheus_client import Counter
from .serializers import StudentSerializer
from ginger.rest_framework import viewsets, status
from ginger.rest_framework.response import Response
from ginger.rest_framework.decorators import action, api_view
from ginger.drf_yasg.utils import swagger_auto_schema
from ginger.drf_yasg import openapi
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

requests_total = Counter(
    name="health_check_total_3",
    documentation="Total number of various requests. - health check",
    labelnames=["endpoint", "method", "user"],
)


def test_view():
    """Test view"""
    return JsonResponse({"ok": "yes"})


class TestReponseSerializer(serializers.Serializer):
    """test model"""

    text = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


@swagger_auto_schema(method="GET", responses={200: openapi.Response("testResponse", TestReponseSerializer)}, security=[{"Bearer": []}])
@api_view(["GET"])
def test_view2(request):
    """Test view"""
    requests_total.labels(endpoint="Test view 2", method=test_view2, user=None).inc()
    return JsonResponse({"text": "Just rendering some JSON :)"})


@cache_page(10)
def health_check_view(request):
    """Server health check request handler"""
    requests_total.labels(endpoint="Health check", method=health_check_view, user=None).inc()
    now = datetime.now()
    return JsonResponse({"status": "ok", "server_time": now.strftime("%d/%m/%Y, %H:%M:%S")})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @swagger_auto_schema(
        method='get',
        responses={200: StudentSerializer(many=True)},
        security=[{"Bearer": []}]
    )
    @action(detail=False, methods=['get'])
    def list_students(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='post',
        request_body=StudentSerializer,
        responses={201: StudentSerializer},
        security=[{"Bearer": []}]
    )
    @action(detail=False, methods=['post'])
    def create_student(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='get',
        responses={200: StudentSerializer},
        security=[{"Bearer": []}]
    )
    @action(detail=True, methods=['get'])
    def retrieve_student(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='put',
        request_body=StudentSerializer,
        responses={200: StudentSerializer},
        security=[{"Bearer": []}]
    )
    @action(detail=True, methods=['put'])
    def update_student(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='delete',
        responses={204: 'No Content'},
        security=[{"Bearer": []}]
    )
    @action(detail=True, methods=['delete'])
    def delete_student(self, request, pk=None):
        student = self.get_object()
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
