import datetime
import flask
import glob
import pandas as pd
import os
from datetime import date

i=0

app=flask.Flask("kanban")

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1


    return len(string) - len(parts[-1]) - len(substring)

def get_html(page_name):
    html_file=open(page_name+".html")
    content=html_file.read()
    html_file.close()
    return content


@app.route("/")
def log_in():
    return get_html("template/index")
    

@app.route("/kanban")
def home():
    directory=list(glob.glob("*.txt"))
    actual_values_open=""
    actual_values_closed=""
    file=open('button1.txt','r')
    button1=file.read()
    file.close()
    file=open('button2.txt','r')
    button2=file.read()
    file.close()
    file=open('task.txt','r')
    task_class=file.read()
    file.close()
    file=open('task_late.txt','r')
    task_class_late=file.read()
    file.close()

    for i in range(len(directory)):
        task_details=directory[i]
        file=open(task_details,'r')
        task_note=file.read()
        file.close()
        first_=task_details.find("_")
        second_=findnth(task_details,"_",1)
        third_=findnth(task_details,"_",2)
        owner=task_details[first_+1:second_]
        deadline=task_details[second_+1:third_]
        status=task_details[0:4]
        char_num=len(task_details)
        id=task_details[char_num-10:]
        today = date.today()
        today_date=today.strftime("%Y-%m-%d")
        if(status=='todo' and deadline>today_date):
            actual_values_open+= "<div"+task_class+"<p>"+task_note+"</p>"+"<p>"+owner+"</p>"+"<p>"+deadline+"</p>"+"<p>"+button1+id+" "+button2+"</p>"+"</div>"
        if(status=='todo'and today_date>=deadline):
            actual_values_open+= "<div"+task_class_late+"<p>"+task_note+"</p>"+"<p>"+owner+"</p>"+"<p>"+deadline+"</p>"+"<p>"+button1+id+" "+button2+"</p>"+"</div>"
        
        if(status=='done'):
            actual_values_closed+= "<div"+task_class+"<p>"+task_note+"</p>"+"<p>"+owner+"</p>"+"<p>"+deadline+"</p>"+"<p>"+"</div>"
    html_page=get_html("template/kanban")
    return html_page.replace("$$ALL OPEN$$",actual_values_open).replace("$$ALL COMPLETED $$",actual_values_closed)


@app.route("/add_task")
def add_task():
    html_page=get_html("template/add_task")
    today = date.today()
    today_date=today.strftime("%Y-%m-%d")
    return html_page.replace("$$DATE$$",today_date)


@app.route("/task_created")
def task_created():
    who=flask.request.args.get("All")
    due_date=flask.request.args.get("d")
    task_det=flask.request.args.get("t")
    date=str(datetime.datetime.now()).replace(" ","_").replace(".","_").replace(":","_")
    newnote="todo"+"_"+who+"_"+due_date+"_"+date
    name=newnote +".txt"
    file=open(name,"w")
    file.write(task_det)
    file.close()
    return get_html("template/task_created")

@app.route("/task_completed")
def task_completed():
    identifier=flask.request.args.get("to_clean")
    directory=list(glob.glob("*.txt"))
    directory.remove('button1.txt')
    directory.remove("button2.txt")
    directory.remove("task.txt")
    directory.remove("task_late.txt")
    i=0
    for i in range(len(directory)):
        case=directory[i]
        string_len=len(case)
        match=directory[i][string_len-10:]
        print(match)
        print(identifier)
        print("")

        if (match==identifier):
            newname="done_"+directory[i][5:]
            file=open(directory[i],'r')
            task_note=file.read()
            file.close()
            file=open(newname,'w')
            file.write(task_note)
            file.close()
            os.remove(directory[i])

    return get_html("template/task_completed")

@app.route("/all_clean")
def clean_complete():
    
    directory=list(glob.glob("*.txt"))
    directory.remove('button1.txt')
    directory.remove("button2.txt")
    for i in range(len(directory)):
        match=directory[i][0:4]
        print(match)
        if (match=="done"):
            os.remove(directory[i])
    return get_html("template/all_clean")
        


        

            


