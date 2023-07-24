from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Users, Messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# from static.images import views


# Create your views here.


def loginform(request):
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

        messages.success(request, 'Registration successful')

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

    messages.success(request, 'User deleted successfully')

    return redirect("/viewdata")


def viewMessages(request):
    viewmessages = Messages.objects.all()
    context = {"viewmessages": viewmessages}

    return render(request, 'viewmessages.html', context)


def deleteMessage(request, id):
    deleteMessage = Messages.objects.get(id=id)
    deleteMessage.delete()

    messages.success(request, 'Message deleted successfully')

    return redirect("/viewmessages")


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

        messages.success(request, "User updated successfully")
        return redirect("/viewdata")



    d = Users.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edituser.html', context)


def shop(request):
    return render(request, 'shop.html')


def signup(request):
    return render(request, 'signup.html')


def signupdata(request):
    if request.method == 'POST':
        username = request.POST.get('s-name')
        email = request.POST.get('s-email')
        password = request.POST.get('s-password')

        signup = User.objects.create_user(username, email, password)
        signup.save()
    return redirect('/login')


def userlogin(request):
    if request.method =="POST":
        l_username = request.POST.get('login-username')
        l_password = request.POST.get('login-password')
        userlog = authenticate(username=l_username, password=l_password)
        if userlog is not None:
            login(request, userlog)
            return redirect('/')
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('/login')

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashlayout.html')


def viewvehicle(request):
    return render(request, 'viewvehicle.html')

def cart(request):
    return render(request, 'cart.html')


def uploads(request):
    return render(request, 'uploads.html')









