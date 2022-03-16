from asyncio.windows_events import NULL
from tabnanny import verbose
from django.db import models
from accounts.models import ProfileModel

class concertModel (models.Model):
    class Meta:
        verbose_name="کنسرت"
        verbose_name_plural="کنسرت"
    Name=models.CharField(max_length=100,verbose_name="نام کنسرت")
    SingerName=models.CharField(max_length=100,verbose_name="خواننده")
    lenght=models.IntegerField(verbose_name="مدت")
    poster=models.ImageField(upload_to="concertImages/",null=True,verbose_name="پوستر")

    def __str__(self):
        return self.SingerName

class locationModel(models.Model):
    class Meta:
        verbose_name="محل برگزاری"
        verbose_name_plural="محل برگزاری"
    IdNumber=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100,verbose_name="نام محل")
    Address=models.CharField(max_length=500,default="تهران - برج میلاد",verbose_name="آدرس")
    phone=models.CharField(max_length=11,null=True,verbose_name="تلفن")
    capacity=models.IntegerField(verbose_name="ظرفیت")


    def __str__(self):
        return self.Name


class timeModel(models.Model):
    class Meta:
        verbose_name="سانس"
        verbose_name_plural="سانس"

    concertModel=models.ForeignKey(to=concertModel,on_delete=models.PROTECT,verbose_name="کنسرت")
    locationModel=models.ForeignKey("locationModel",on_delete=models.PROTECT,verbose_name="محل برگزاری")

    StartDateTime=models.DateTimeField(verbose_name="تاریخ برگزاری")
    Seats=models.IntegerField(verbose_name="تعداد صندلی")
    Start=1
    End=2
    Cancle=3
    Sales=4
    Status_choice=((Start,"فروش بلیط شروع شده است"),
                    (End,"فروش بلیط تمام شده است"),
                    (Cancle,"این سانس کنسل شده است"),
                    ( Sales,"در حال فروش بلیط"))
    Status=models.IntegerField(choices=Status_choice,verbose_name="وظعیت")
    def __str__(self):
        return f"Time : {self.StartDateTime} concertname :{self.concertModel.Name} Location :{self.locationModel.Name}"
    




class ticketModel(models.Model):
    class Meta:
        verbose_name="بلیط"
        verbose_name_plural="بلیط"
    ProfileModel=models.ForeignKey(ProfileModel,on_delete=models.PROTECT,verbose_name="کاربر")
    timeModel=models.ForeignKey("timeModel",on_delete=models.PROTECT,verbose_name="سانس")
    Name=models.CharField(max_length=100,verbose_name="عنوان")
    price=models.IntegerField(verbose_name="مبلغ")
    ticketImage=models.ImageField(upload_to="TicketImages/",verbose_name="عکس")

    def __str__(self):
        return f"TicketInfo : Profile: ConcertInfo : {timeModel.__str__()}"
 