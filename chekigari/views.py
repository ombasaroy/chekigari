from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Users, Messages
from django.contrib import messages


# from static.images import views


# Create your views here.


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def viewdata(request):
    data = Users.objects.all()

    context = {"data": data}

    return render(request, 'view.html', context)


def contact(request):
    return render(request, 'contact.html')


def insert(request):
    if request.method == 'POST':
        fname = request.POST.get('first-name').title()
        onames = request.POST.get('other-names').title()
        phone = request.POST.get('tel-no')
        dob = request.POST.get('dob')
        email = request.POST.get('email').lower()
        country = request.POST.get('country')
        gender = request.POST.get('gender')
        reg = Users(fname=fname, onames=onames, phone=phone, dob=dob, email=email, country=country, gender=gender)
        reg.save()

    return redirect('/register')


def sendMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone_no')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        query = Messages(name=name, phone=phone, subject=subject, message=message)
        query.save()
        messages.success(request, 'Message sent successfully')

    return render(request, 'contact.html')


def delete(request, id):
    d = Users.objects.get(id=id)
    d.delete()

    return redirect("/viewdata")


def viewMessages(request):
    messages = Messages.objects.all()
    context = {"messages": messages}

    return render(request, 'viewmessages.html', context)


def deleteMessage(request, id):
    deleteMessage = Messages.objects.get(id=id)
    deleteMessage.delete()

    return redirect("/messages")


def edituser(request, id):
    if request.method == "POST":
        fname = request.POST['first-name']
        onames = request.POST['other-names']
        phone = request.POST['tel-no']
        dob = request.POST['dob']
        email = request.POST['email']
        country = request.POST['country']
        gender = request.POST['gender']

        update = Users.objects.get(id=id)
        update.fname = fname
        update.onames = onames
        update.phone = phone
        update.dob = dob
        update.email = email
        update.country = country
        update.gender = gender

        update.save()

    d = Users.objects.get(id=id)
    context = {"d":d}
    return render(request, 'edituser.html', context)


def shop(request):
    return render(request, 'shop.html')
