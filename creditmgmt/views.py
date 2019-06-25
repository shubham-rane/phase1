from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from creditmgmt.models import Usercredits

# Create your views here.
def viewusers(request):
	users=Usercredits.objects.all()
	return render(request,'creditmgmt/viewusers.html',{'obj':users})

def transfer(request):
	user_id=request.POST['credits']
	user=Usercredits.objects.get(id=user_id)
	print(user.name)
	return render(request,'creditmgmt/transfer.html',{'user':user})

def update(request):
	reciever_name=request.POST['reciever']
	amt=request.POST['amt']
	sender_id=request.POST['sender']
	
	sender=Usercredits.objects.get(id=sender_id)
	reciever=Usercredits.objects.get(name=reciever_name)
	print(sender.credits,reciever.credits)
	if int(amt)<int(sender.credits):
		sender.credits-=int(amt)
		sender.save()
		reciever.credits+=int(amt)
		reciever.save()
	

	users=Usercredits.objects.all()

	return render(request,'creditmgmt/viewusers.html',{'obj':users})

def adduser(request):
	name=request.POST['name']
	credits=request.POST['credits']
	user=Usercredits(name=name,credits=credits)
	user.save()

	users=Usercredits.objects.all()
	return render(request,'creditmgmt/viewusers.html',{'obj':users})
	



