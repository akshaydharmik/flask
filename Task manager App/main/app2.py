from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import datetime; date = datetime.date



app2 = Flask(__name__)
app2.secret_key = "Secret Key"

app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app2)

class Todoupdated(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    priority = db.Column(db.String(100))
    duedate = db.Column(db.Text)

    def __init__(self, name, description, priority, duedate):

        self.name = name
        self.description = description
        self.priority = priority
        self.duedate=duedate



@app2.route('/',methods=['GET', 'POST'])
def index():

    all_data=Todoupdated.query.all()
    # you can run the below command to create tablein our database initially during first run
    # or you can use command prompts python--> from app1 impot db --> db.create_all()
    # db.create_all()
    return render_template("index1.html", employees=all_data)


@app2.route('/insert',methods=['GET', 'POST'])
def insert():

    if request.method=='POST':
        name=request.form['name']
        description = request.form['description']
        priority = request.form['priority']
        duedate = request.form['duedate']

        my_data=Todoupdated(name ,description ,priority,duedate)
        db.session.add(my_data)
        db.session.commit()
        flash('Task added Successfully')

        return redirect(url_for('index'))

@app2.route('/update',methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Todoupdated.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.description = request.form['description']
        my_data.priority = request.form['priority']
        my_data.duedate = request.form['duedate']
        duedate = request.form['duedate']


        db.session.commit()
        flash("Task Updated Successfully")

        return redirect(url_for('index'))


@app2.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data=Todoupdated.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Task Deleted successfully")

    return redirect(url_for('index'))



if __name__ == "__main__":
    app2.run(debug=True)