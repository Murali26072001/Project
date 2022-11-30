from django.db import models
class Student_Details(models.Model):
	User_Name=models.CharField(max_length=100,primary_key=True)
	Regno=models.IntegerField(unique=True)
	Name =models.CharField(max_length=100)
	DOB=models.DateField()
	Gender=models.CharField(max_length=50)
	Department=models.CharField(max_length=100)
	Mail_ID=models.EmailField(max_length = 254)
	Photo=models.ImageField(upload_to ='Student_Images/')
	Biometric=models.ImageField(upload_to ='Student_Biometric/')	
	class Meta:
		db_table="Student_Details"
class Staff_Details(models.Model):		
	User_Name=models.CharField(max_length=100,primary_key=True)
	Staff_ID=models.IntegerField(unique=True)
	Name =models.CharField(max_length=100)
	Department =models.CharField(max_length=100)
	Mail_ID=models.EmailField(max_length = 254)
	Photo=models.ImageField(upload_to ='Staff_Images/')	
	class Meta:
		db_table="Staff_Details"
	 
# Create your models here.
 
