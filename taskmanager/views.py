import MySQLdb
from django.shortcuts import render, redirect

# Create your views here.
# listing tasks
def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,task_no,task_desc FROM taskmanager_task")
        tasks = cursor.fetchall()
    return render(request, 'task/index.html', {'tasks': tasks})

# add new tasks
def add(request):
    if request.method == 'GET':
        return render(request, 'task/add.html')
    else:
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO taskmanager_task (task_no,task_desc) "
                           "values (%s,%s)", [task_no, task_desc])
            conn.commit()
        return redirect('../')


# update task info
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,task_no,task_desc FROM taskmanager_task where id =%s", [id])
            task = cursor.fetchone()
        return render(request, 'task/edit.html', {'task': task})
    else:
        id = request.POST.get("id")
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE taskmanager_task set task_no=%s,task_desc=%s where id =%s",
                           [task_no, task_desc, id])
            conn.commit()
        return redirect('../')

# delete a task
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM taskmanager_task WHERE id =%s", [id])
        conn.commit()
    return  redirect('../')