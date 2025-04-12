from django.shortcuts import render
from django.http import HttpResponse

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def employee_list(request):
    return render(request, 'admin/employee_list.html')

def employee_detail(request, employee_id):
    return render(request, 'admin/employee_detail.html', {'employee_id': employee_id})