import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, ProfileForm
from .models import profile
from django.core.mail import EmailMessage
from mysite import settings

code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        pform = ProfileForm(request.POST)
        if form.is_valid() and pform.is_valid():
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birthday = pform.cleaned_data.get('birthday')
            user = User.objects.create_user(username=email, password=raw_password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            p = profile(user=user, birthday=birthday, is_email_verified=False)
            p.save()
            login(request, user)
            return redirect('emailVer')
    else:
        form = SignupForm()
        pform = ProfileForm()
    return render(request, 'authUser/signup.html', {'form': form, 'pform': pform})

def emailVer(request):
    subject="Verification"
    message = f"{code}"
    email_from = settings.EMAIL_HOST_USER
    email_to = [request.user.email, ]
    print(request.user.email)
    msg = EmailMessage(
        subject,
        message,
        from_email=email_from,
        to=email_to,
    )
    msg.send(fail_silently=False)

    if request.method == 'GET':
        return render(request, 'authUser/codeCheck.html')
    else:
        if request.POST['code'] == code:
            pro = profile.objects.get(user=request.user)
            print(request.user)
            print(pro)
            pro.is_email_verified = True
            pro.save()
            return redirect('home')
        else:
            return render(request, 'authUser/codeCheck.html', {'error': 'Code did not work, sent another code please check your email again!'})

