from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    form = Form.objects.all()

    if request.method=="POST":
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        message= request.POST.get('message')

        Form.objects.create(
            name=name,
            phone= phone,
            email= email,
            message= message
        )

        # Send an email
        subject = 'New Form Submission'
        message_body = f'You have received a new mail from {name}:\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['dipendra.kafle@study.lbef.edu.np']

        send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)

        messages.success(request, 'Your message has been sent to Dipendra Kafle.')

        return redirect("/")
    return render(request, "home/index.html")
