from flask import Flask, render_template, request
from gpa import main
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)



@app.route("/")
def index():
    main()
    return render_template("gpa.html")


@app.route('/', methods=['POST'])
def login():
    print()


if __name__ == "__main__":
    app.run('localhost', 8080) 




'''@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    global gpa1
    gpa1 = main(username, password)
    return render_template("gpa.html", finalgpa = round(gpa1, 3))


@app.route('/gpa', methods=['GET', 'POST'])    
def gpa():
    subject = request.form.get("subject")
    level = request.form.get("level")
    grade = request.form.get("grade")
    credits = request.form.get("credits")
    return render_template("gpa.html", finalgpa = gpa1)'''

    

