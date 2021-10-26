
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer 




# Create your views here.

class EmpployeesList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer