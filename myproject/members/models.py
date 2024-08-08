from django.db import models
# Create your models here.
class signup1(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    ph=models.IntegerField()
    pwd=models.CharField(max_length=12)
    cpwd=models.CharField(max_length=12)
    def __str__(self):
         return self.fname

class signup2(models.Model):
    uname=models.CharField(max_length=20,default='')
    email=models.CharField(max_length=40)
    mobile=models.IntegerField()
    password=models.CharField(max_length=12)
    cpassword=models.CharField(max_length=12)
    def __str__(self):
      return self.email or ''

class organizers(models.Model):
    name1=models.CharField(max_length=20)
    email1=models.CharField(max_length=40)
    mobile1=models.IntegerField()
    ename=models.CharField(max_length=20)
    etype=models.CharField(max_length=100)
    eloc=models.CharField(max_length=100)
    etheme=models.CharField(max_length=60)
    epic=models.ImageField(upload_to='images/',null=True)
    ereq=models.CharField(max_length=100)
    ebudget=models.IntegerField()
    ebreak=models.IntegerField()
    eservice=models.CharField(max_length=100)
    experience=models.IntegerField(default=0)
    ref=models.CharField(max_length=100,default='')
    def __str__(self):
         return self.name1
    
class book(models.Model):
    email=models.ForeignKey(signup2,on_delete=models.CASCADE,default=None)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=20)
    gcount=models.IntegerField()
    addreq=models.CharField(max_length=100)

    def __str__(self):
     return str(self.email) 


    




