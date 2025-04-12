from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the HRMS Client Dashboard")

def employee_list(request):
    # Logic to retrieve and display a list of employees
    return HttpResponse("List of Employees")

def employee_detail(request, employee_id):
    # Logic to retrieve and display details of a specific employee
    return HttpResponse(f"Details of Employee {employee_id}")