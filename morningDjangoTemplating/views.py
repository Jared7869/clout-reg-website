from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def gallery(request):
    return render(request,'gallery.html')

mycourses = [
    {"name": "Python", "duration": "2 months","cost":"ksh. 25k"},
    {"name": "Android", "duration": "4 months", "cost": "ksh. 30k"},
    {"name": "Datascience", "duration": "8 months", "cost": "ksh. 45k"},
]


def courses(request):
    context = {"mycourses": mycourses}
    return render(request, 'courses.html', context)
