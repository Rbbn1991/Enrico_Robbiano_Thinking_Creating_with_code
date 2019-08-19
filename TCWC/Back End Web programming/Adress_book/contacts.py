import flask
app=flask.Flask("contacts")


def get_html(page_name):
    html_file=open(page_name+".html")
    content=html_file.read()
    html_file.close()
    return content

def get_contacts():
    peopledb=open("people.txt")
    content=peopledb.read()
    peopledb.close()
    people=content.split("\n")
    people.pop(len(people)-1)
    return people

@app.route("/")
def home():
    return get_html("index")

@app.route("/people")
def people():
    html_page= get_html("people")
    people=get_contacts()

    actual_values=""
    for person in people:
        actual_values+= "<p>"+ person +"<p>"
return html_page.replace("$$PEOPLE$$",actual_values)


@app.route("/search")
def search():
    html_page=get_html("people")
    query= flask.request.args.get("q")
    people=get_contacts()
    results=""
    for person in people:
        if person.lower().find(query.lower())!= -1:
            results += "<p> No results found </p>"
        if results=="":
            results="<p> No result found </p>"
    return html_page.replace("$$PEOPLE$$", results)