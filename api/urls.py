from django.urls import path
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('employees/', views.EmpployeesList.as_view()),
    path('employees/<str:pk>', views.EmployeesDetail.as_view())
    
]