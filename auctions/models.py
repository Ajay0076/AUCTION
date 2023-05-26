from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
class Player(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    mobilenumber= models.IntegerField(default=1)
    currentclub=models.CharField(max_length=64)
    Age=models.IntegerField(default=1)
    position=models.CharField(max_length=10,default="a")
    password=models.CharField(max_length=20)
    image_url = models.ImageField(max_length=228, default=None, blank=True, null=True)
    base=models.IntegerField(default=1000)
    def __str__(self):
        return self.username
class Club(models.Model):
    clubname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    contactNo= models.IntegerField(default=1)
    manager=models.CharField(max_length=64)
    place=models.CharField(max_length=64)
    password=models.CharField(max_length=20)
    logo=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.clubname
class auction(models.Model):
    title = models.CharField(max_length=64)   
    image_url = models.ImageField(max_length=228, default = None, blank = True, null = True)
    deadline=models.DateField(default = None, blank = True, null = True)
    status=models.CharField(max_length=20,default='No')
    end=models.DateField(default = None, blank = True, null = True)
    def __str__(self):
        return self.title
class auctionreg(models.Model):
    auction=models.ForeignKey(auction,on_delete=models.CASCADE,blank = True, null = True)
    clubname = models.ForeignKey(Club,on_delete=models.CASCADE,blank = True, null = True)
    playername = models.ForeignKey(Player,on_delete=models.CASCADE,blank = True, null = True)
    status=models.CharField(max_length=20,default='Unknown')
class bidplayer(models.Model):
    auction=models.ForeignKey(auction,on_delete=models.CASCADE,blank = True, null = True)
    clubname = models.ForeignKey(Club,on_delete=models.CASCADE,blank = True, null = True)
    playername = models.ForeignKey(Player,on_delete=models.CASCADE,blank = True, null = True)
    amount=models.IntegerField()
class Acceptdeal(models.Model):
    clubname = models.ForeignKey(Club,on_delete=models.CASCADE,blank = True, null = True)
    playername = models.ForeignKey(Player,on_delete=models.CASCADE,blank = True, null = True)
    status=models.CharField(max_length=20,default='No')


