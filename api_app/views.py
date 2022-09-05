from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer
from .models import DemoStudent


# Create your views here.
class TestArea(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Bernard Iorver',
            'age': 27,
            'sex': 'male'
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = request.data
        if data:
            return Response(data)
        return Response("No Data Supplied")


class StudentApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        query_set = DemoStudent.objects.all()
        serializer = StudentSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
