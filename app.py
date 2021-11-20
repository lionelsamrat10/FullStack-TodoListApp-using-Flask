from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # Creating the Flask class object

# Configuring the Database
# SQLAlchemy is an ORM Tool
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Creating the Todo Class
# This class will be used to store the details of the Todos
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  
    
    # Similar to toString() in Java
    # Used to print details of the Object of the Todo Class
    def __repr__(self):
        return f"{self.sno} - {self.title} - {self.desc}"

@app.route('/todos', methods=['POST', 'GET'])
def home_todos():
    # Handling the POST Request
    # The POST request is used to craete the Todos
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)
    # This render_template function takes the file from the templates folder and renders it
    return render_template('index.html', allTodo=allTodo)

@app.route('/show-todos')
def show_todos():
    allTodo = Todo.query.all()
    print(allTodo)
    return "Returning all todos"

if __name__ == '__main__':
    app.run(debug=True, port=8000)