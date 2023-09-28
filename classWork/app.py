from flask import Flask, request,render_template,url_for,redirect

app=Flask(__name__)
names=[]

@app.route("/")
def home():
    return render_template('./index.html',names=names)

@app.route("/add_task",methods=['POST'])
def add_task():
    name=request.form['name']
    if name:
        names.append(name)
    return redirect(url_for('home'))
