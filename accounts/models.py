from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربر"

    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="کاربری",related_name="profile")
    # Name=models.CharField(max_length=100,verbose_name="نام")
    # Family=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    ProfileImage=models.ImageField(upload_to="ProfileImages/",verbose_name="عکس")
    Man=1
    Woman=2
    status_choice=((Man,"مرد"),(Woman,"زن"))
    Gender=models.IntegerField(choices=status_choice,verbose_name="جنسیت")
    credit=models.IntegerField(verbose_name="اعتبار",default=0)



    