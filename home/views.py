from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST["title"]
        desc=request.POST["desc"]
        # print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context={'success':True}

    return render(request,"index.html",context)
def tasks(request):
    alltasks=Task.objects.all()
    context ={'tasks':alltasks}
    # print(alltasks)
    return render(request,"tasks.html",context)