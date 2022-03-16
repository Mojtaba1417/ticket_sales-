from audioop import reverse
from multiprocessing import context
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from accounts.models import ProfileModel
import ticketSales
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import ProfileRegisterForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            
        else:
            context={
                "username":username,
                "errorMessage":"کاربری با این مشخصات یافت نشد "
            } 
            return render(request,"accounts/login.html",context)
    else:
        return render(request,"accounts/login.html",{})
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
@login_required
def profileView(request):
    profile=request.user.profile

    context={
        "profile":profile
    }
    return render(request,"accounts/profile.html",context)
# @api_view(["POST"])
def profileRegisterView(request):
    if request.method=="POST":
        # serializer=UserSerializer(data=request.data)
        # data={}
        # if serializer.is_valid():
        #     user=serializer.save()
        #     data["message"]="ثبت نام با موفقیت انجام شد ."
        #     data['token']=Token.objects.get(user=user).key
        
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():
            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],email=profileRegisterForm.cleaned_data['email'],password=profileRegisterForm.cleaned_data['password'],first_name=profileRegisterForm.cleaned_data['first_name'],
            last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=ProfileModel(user=user,ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],Gender=profileRegisterForm.cleaned_data['Gender'],credit=profileRegisterForm.cleaned_data['credit'])
            profileModel.save()

            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        profileRegisterForm=ProfileRegisterForm


    context={
        "formData":profileRegisterForm
    }
    return render(request,"accounts/profileRegister.html",context)