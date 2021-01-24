from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
# this validation is contact form
	if request.method=="POST":
		message_name=request.POST['message-name']
		message_email=request.POST['message-email']
		message=request.POST['message']

		#this validation is contact form send in email
		send_mail(
			message_name, #Subject
			message, #Message
			message_email, #From Email
			['example@gmail.com'], #To Email
			)

		return render(request,"home.html",{'message_name':message_name})
	else:
		return render(request,"home.html",{})

def appointment(request):
# this validation is contact form
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		day=request.POST['day']
		time=request.POST['time']
		doctor=request.POST['doctor']
		msg=request.POST['msg']

		#this validation is appointment form send in email
		appointment="Name:" + name + "Email:" + email + "Day:" + day + "Time:" + time + "Doctor:" + doctor + "Message:" + msg
		send_mail(
		 	'Appointment Request',
		 	appointment,
			email, #From Email
		 	['example@gmail.com'], #To Email
		 	)

		return render(request,"appointment.html",{
			'name':name,
			'email':email,
			'day':day,
			'time':time,
			'doctor':doctor,
			'msg':msg
			})
	else:
		return render(request,"home.html",{})