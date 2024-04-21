from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    Employee_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='pending')  # pending/approved/rejected
    # Add other fields as needed
