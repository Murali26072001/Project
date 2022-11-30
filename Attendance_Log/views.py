from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from .models import Staff_Details
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
def login(request):
	username=request.POST.get("usr")
	password=request.POST.get("psd")	
	user = authenticate(username=username, password=password)	
	if user is not None:
		#login(request,user)
		a=list(User.objects.all().values("username"))
		l=[]
		for i in range(len(a)):
			l.append(a[i].get("username"))
		context={'title': l}	
		return render(request,"Staff_Info.html",context)
	else:    
    		context={'title': 'Invalid Username or Password'}
    		return render(request, 'index.html',context)
class Staff:
	def Add_Staff(request): 		
		if request.method == 'POST' and request.FILES['upload']:
			upload = request.FILES['upload']
			fss = FileSystemStorage()
			file = fss.save('images/Staff_Images/'+upload.name, upload)
			file_url = fss.url(file)
			User_Name=request.POST.get("User_Name")
			staff_id=request.POST.get("Staff ID")
			staff_name=request.POST.get("Staff Name")
			staff_dep=request.POST.get("Staff Department")
			staff_Mail=request.POST.get("Staff Mail_ID")
			staff=Staff_Details(User_Name=User_Name,Staff_ID=staff_id,Name=staff_name,
			Department=staff_dep,Mail_ID=staff_Mail,
			Photo='images/Staff_Images/'+upload.name)
			staff.save()	
			return render(request, 'Staff_Info.html', {'file_url': file_url})
		return render(request, 'Staff_Info.html')  	

# Create your viws here.conte    
    
    
    
    
