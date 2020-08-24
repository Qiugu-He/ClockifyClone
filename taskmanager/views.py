import MySQLdb
from django.shortcuts import render, redirect

# Create your views here.
# listing tasks
def index(request):
    try:
        # get total # of tasks
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,task_no,task_desc FROM taskmanager_task")
            tasks = cursor.fetchall()

        # get total counts of entry
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM taskmanager_task")
            records = cursor.fetchall()
        context = {
            'tasks': tasks,
            'count': len(records),
        }
        return render(request, 'task/index.html', context)
        cursor.close()

    except MySQLdb.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (conn):
            conn.close()
            print("MySQL connection is closed")

# add new tasks
def add(request):
    if request.method == 'GET':
        return render(request, 'task/add.html')
    else:
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')

        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
            with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute("INSERT INTO taskmanager_task (task_no,task_desc) "
                               "values (%s,%s)", [task_no, task_desc])
                conn.commit()
            return redirect('../')
            cursor.close()

        except MySQLdb.Error as error:
            print("Failed to read data from table", error)
        finally:
            if (conn):
                conn.close()
                print("MySQL connection is closed")

# update task info
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
            with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute("SELECT id,task_no,task_desc FROM taskmanager_task where id =%s", [id])
                task = cursor.fetchone()
            return render(request, 'task/edit.html', {'task': task})
            cursor.close()

        except MySQLdb.Error as error:
            print("Failed to read data from table", error)
        finally:
            if (conn):
                conn.close()
                print("MySQL connection is closed")
    else:
        id = request.POST.get("id")
        task_no = request.POST.get('task_no', '')
        task_desc = request.POST.get('task_desc', '')
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
            with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute("UPDATE taskmanager_task set task_no=%s,task_desc=%s where id =%s",
                               [task_no, task_desc, id])
                conn.commit()
            return redirect('../')
            cursor.close()

        except MySQLdb.Error as error:
            print("Failed to read data from table", error)
        finally:
            if (conn):
                conn.close()
                print("MySQL connection is closed")

# delete a task
def delete(request):
    id = request.GET.get("id")
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="clockifyclone", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("DELETE FROM taskmanager_task WHERE id =%s", [id])
            conn.commit()
        return  redirect('../')
        cursor.close()

    except MySQLdb.Error as error:
        print("Failed to read data from table", error)

    finally:
        if (conn):
            conn.close()
            print("MySQL connection is closed")