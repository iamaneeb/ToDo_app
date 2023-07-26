from django.shortcuts import render
from django.utils import timezone
from base.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    todo_list = Todo.objects.all().order_by('-addedtime')
    return render(request,'base/index.html',{
        'todo_list' : todo_list
    })

def add_todo(request):
    content = request.POST['content']
    current_time = timezone.now()
    Todo.objects.create(addedtime = current_time,text = content)
    
   
    return HttpResponseRedirect('/')
