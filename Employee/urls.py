from django.urls import path
from . import views


urlpatterns = [
    path('',views.employee_list,name='employee_list'),
    path('employee/<int:id>/', views.employee_details, name='employee_details'),
    path('employee/create/',views.employee_create,name='employee_create'),
    path('update/<int:id>/', views.employee_update, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    
]