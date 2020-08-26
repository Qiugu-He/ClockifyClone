import MySQLdb
from django.shortcuts import render, redirect
from.models import Task


# ___________ Listing tasks ____________
def index(request):
    # get all tasks
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'count': len(tasks),
    }
    return render(request, 'task/index.html', context)


# ___________ Add new task ____________
def add(request):
    if request.method == 'GET':
        return render(request, 'task/add.html')
    else:
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')

        task = Task(task_no=task_no, task_desc=task_desc)
        task.save()
        return redirect('../')


# ____________ Update task info ____________
def edit(request):
    # populate task information
    if request.method == 'GET':
        taskid = request.GET.get("id")
        task = Task.objects.get(id=taskid)
        return render(request, 'task/edit.html', {'task': task})

    # update information
    else:
        id = request.POST.get("id")
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')

        task=Task.objects.get(id=id)
        task.task_no = task_no
        task.task_desc = task_desc
        task.save()
        return redirect('../')


# delete a task
def delete(request):
    taskid = request.GET.get("id")
    task=Task.objects.get(id=taskid)
    task.delete()
    return redirect('../')
