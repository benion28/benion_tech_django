from rest_framework import serializers
from .models import DemoStudent


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoStudent
        fields = (
            'name', 'age', 'sex'
        )
