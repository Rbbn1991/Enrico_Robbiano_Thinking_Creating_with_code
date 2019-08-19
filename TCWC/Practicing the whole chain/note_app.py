import datetime
import flask
import glob
import pandas as pd

app=flask.Flask("notes")

def get_html(page_name):
    html_file=open(page_name+".html")
    content=html_file.read()
    html_file.close()
    return content

def get_username():
    file=open('username.txt','r')
    written_note=file.read()
    file.close()
    return(len(written_note))

@app.route("/")
def home():
    user=get_username()
    if user==0:
        return get_html("index")
    else:
        html_page=get_html('main_page')
        file=open('username.txt',"r")
        username=file.read()
        file.close()
        results=""
        results+="<h2>"+ username +"</h2>"
        return html_page.replace("$$ username $$",results)

        

@app.route("/note")
def new_note():
    html_page=get_html('note')
    file=open('username.txt',"r")
    username=file.read()
    file.close()
    results=""
    results+="<h2>"+ username +"</h2>"
    return html_page.replace("$$ username $$",results)


@app.route("/note_add")
def note_add():
    html_page=get_html('note_add')
    newnote=flask.request.args.get("t")
    results=""
    date=str(datetime.datetime.now()).replace(" ","_").replace(".","_").replace(":","_")
    name=date +".txt"
    file=open(name,"w")
    file.write(newnote)
    file.close()
    results += "<p>"+ name +"</p>"+"<p>"+ newnote +"</p>"
    return html_page.replace("$$ note $$",results)


@app.route('/all_notes')
def all_note():
    html_page=get_html('all_notes')
    directory=list(glob.glob("*.txt"))
    actual_values=""
    directory.remove('username.txt')
    for i in range(len(directory)):
        note_sing=directory[i]
        file=open(note_sing,'r')
        written_note=file.read()
        file.close()
        actual_values+= "<p>"+ note_sing +"<p>"+"<p>"+ written_note +"<p>"
    return html_page.replace("$$ note $$",actual_values)

@app.route("/search")
def search():
    html_page=get_html('search')
    file=open('username.txt',"r")
    username=file.read()
    file.close()
    results=""
    results+="<h2>"+ username +"</h2>"
    return html_page.replace("$$ username $$",results)
    


@app.route("/search_res")
def search_res():
    html_page=get_html('search_res')
    quest=flask.request.args.get("s")
    directory=list(glob.glob("*.txt"))
    results=""
    directory.remove('username.txt')
    for i in range(len(directory)):
        note_sing=directory[i]
        file=open(note_sing,'r')
        written_note=file.read()
        file.close()
        if written_note.lower().find(quest.lower())!= -1:
            results += "<p>"+note_sing+"</p>"+"<p>"+written_note+"</p>"
    if results=="":
        results +="<p> No results found </p>"
    return html_page.replace("$$ note $$", results)

@app.route("/login")
def login():
    user_input=flask.request.args.get("u")
    name='username.txt'
    file=open(name,"w")
    file.write(user_input)
    file.close()
    
    return get_html("login")

