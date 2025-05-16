from flask import Flask, render_template
from database import get_pictures
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/index')
def about():
    
    return render_template('index.html')
app.run(debug=True)

@app.route('/sindg-up', methods=['GET', 'POST'])
def sing_up():
    if request.metod == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(f"Username: {username}, Email: {email}, Password: {password}")
        add_user(username, email, password)

    return render_template('sing-up.html', title="Регистрация")

def add_user(usernsme, email, password):
    conn = sqlite3.connect('galllery.db')
    cursor = conn.cursor()
    sql = "INSERT INTO user (username, email, password) VALUES (?, ?, ?)"
    cursor.execute(sql, (usernsme, email, password))
    conn.commit()
    conn.close()








