from django.shortcuts import render, redirect
from.models import Task
from datetime import date, timezone


# ___________ Listing tasks ____________
def index(request):
    # get all tasks
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'count': len(tasks)
    }
    return render(request, 'task/index.html', context)


# ___________ Add new task ____________
def add(request):
    task_no = request.POST.get('task_no', '')
    task_desc = request.POST.get('task_desc', '')

    task = Task(task_no=task_no, task_desc=task_desc)
    task.save()
    return redirect('../')


# ____________ Update task info ____________
def edit(request):
    # populate task information
    if request.method == 'GET':
        task_id = request.GET.get("id")
        task = Task.objects.get(id=task_id)
        return render(request, 'task/edit.html', {'task': task})

    # update task information
    else:
        task_id = request.POST.get("id")
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')

        task = Task.objects.get(id=task_id)
        task.task_no = task_no
        task.task_desc = task_desc
        task.save()
        return redirect('../')


# ____________ Delete a task ____________
def delete(request):
    task_id = request.GET.get("id")
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('../')
