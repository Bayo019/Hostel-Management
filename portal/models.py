from django.db import models

GENDERS = [
    ("M", "Male"),
    ("F", "Female")
    
]

HOSTELSTATUS = [
    ("F", "Full"),
    ("H", "Halfway occupied"),
    ("V", "Vaccant")
    
]

class Course(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=25)
    duration = models.IntegerField()
    
    
class Hostel(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=15)
    warden = models.CharField(20) 
    
    
class Room(models.Model):
    capacity = models.IntegerField()
    status = models.CharField(max_length=2, choices = HOSTELSTATUS)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)


class Student(models.Model):
    reg_no = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices = GENDERS)
    address = models.CharField(max_length=100, default = "N/A")
    contact = models.CharField(max_length=10) 
    bed_no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    
    
class Hostel_payment(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.CharField(max_length=10)
    received_by = models.CharField(max_length=20)   
    
    
      
            