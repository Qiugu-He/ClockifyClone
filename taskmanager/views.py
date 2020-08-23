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


from django.shortcuts import render

# Create your views here.
