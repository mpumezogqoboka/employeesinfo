from rest_framework.serializers import ModelSerializer
from .models import Employees

class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
