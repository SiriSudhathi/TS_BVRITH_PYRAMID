from django.db import models

class company_drive(models.Model):
    company_name = models.CharField(max_length=100)

class Shortlisted_students(models.Model):
    student_Id = models.ForeignKey(models, on_delete=models.CASCADE)
    
