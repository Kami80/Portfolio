from django.db import models
from django.utils.timezone import now
import datetime
from faicon.fields import FAIconField
from colorfield.fields import ColorField

# Create your models here.
class MyPage(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(default="-")
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="img/", null=True)

    def __str__(self):
        return self.name

class MyCourses(models.Model):
    course =  models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=200, null=True, blank=True)
    playlist = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="img/courses/", null=True)
    timestamp = models.DateTimeField(default=now)
    tag = models.ManyToManyField("Tag")
    def __str__(self):
        return self.course

class Tag(models.Model):
    tag  = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.tag
    
class Info(models.Model):
    user = models.OneToOneField(MyPage, on_delete=models.CASCADE)
    website = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="img/", null=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)

    def age(self):
        
        return int((datetime.date.today() - self.user.dob).days / 365.25  )
    age = property(age)
    def __str__(self):
        return self.website

class Skill(models.Model):
    user = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200, null=True, blank=True)
    persentage = models.IntegerField(default=100)
    color = ColorField(default='#FFFF00', null=True)
    def __str__(self):
        return self.skill

class Interest(models.Model):
    user = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    interest = models.CharField(max_length=200, null=True, blank=True)
    icon = FAIconField()
    icon_text = models.CharField(max_length=200, null=True, blank=True)
    color = ColorField(default='#FFFF00', null=True)
    def __str__(self):
        return self.interest

class Resume(models.Model):
    user = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    choice = models.CharField(max_length=200, null=True, blank=True, choices=(("Education", "Education"), ("Experience", "Experience")))
    position = models.CharField(max_length=500, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title
    
class More(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    more = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.resume.title

class Blog(models.Model):
    user = models.ForeignKey(MyPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    short = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="img/blogs/", null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.title