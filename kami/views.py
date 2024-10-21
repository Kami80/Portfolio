from django.shortcuts import render
from .models import MyCourses, MyPage, Info, Interest, Skill, Resume, More, Tag, Blog

# Create your views here.

def page(request):

    me = MyPage.objects.get(name = "Kamyab Safaei")
    courses = MyCourses.objects.filter(author__name = "Kamyab Safaei")
    interests = Interest.objects.filter(user__name = "Kamyab Safaei")
    for interest in interests:
        interest.icon_text = str(interest.icon).split(":")[-1]
    skills = Skill.objects.filter(user__name = "Kamyab Safaei")
    a = int(len(skills)/2)
    skills_1 = skills[:a]
    skills_2 = skills[a:]
    info = Info.objects.get(user__name = "Kamyab Safaei")
    educations = Resume.objects.filter(choice = "Education")
    experiences = Resume.objects.filter(choice = "Experience")
    blogs = Blog.objects.filter(user__name = "Kamyab Safaei")
    tags = Tag.objects.all()
    context = {
        "courses": courses,
        "interests":interests,
        "skills1":skills_1,
        "skills2":skills_2,
        "info":info,
        "educations":educations,
        "experiences":experiences,
        "me":me,
        "tags":tags,
        "blogs":blogs,
        
    }

    return render(request, 'index.html', context)

def blog(request):

    return render(request, 'portfolio-details.html')