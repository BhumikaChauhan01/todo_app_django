from django.shortcuts import render,redirect
from .models import Todo,Profile
# Create your views here.

def home(request):
    return render(request,"home.html")


def todo(request):
    result = Todo.objects.filter(is_completed=False)
    parameters ={
        "result" : result   # isme koi bhi completed todo nhi h
    }
    
    return render(request,"todo.html",parameters)  # isme jo parameter ja rha h usme bhi koi completed todo nhi h


def add_todo(request):
    if request.method == "POST":
        
        # Template s view m data la rhi hu
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        # View vala data model m save kr rhi hu
        new_todo = Todo(task=user_task, created_at=user_created_at)
        new_todo.save()
        
        return redirect("todo")
    return render(request,"add_todo.html")


def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")


def update_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        todo.task = user_task
        todo.created_at = user_created_at
        
        todo.save()
        
        return redirect("todo")
    
    parameters = {
        'todo': todo }
    
    return render(request, "update_todo.html", parameters)


def mark_complete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)#for fetching the data with id 
    todo.is_completed=True
    todo.save()
    return redirect("todo")


def upload_profile_pic(request):
    if request.method == "POST":
        profile_pic= request.FILES["profile_pic"]
        new_profile = Profile(
            title= "demo_student",
            profile_pic =profile_pic
        )
        new_profile.save()
        return redirect("todo")


    return render(request,"upload_profile_pic.html")


