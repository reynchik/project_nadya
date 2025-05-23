from flask import Flask, render_template
# from database import get_pictures
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        place = request.form["place"]
        
        creature = request.form["creature"]
        fur = request.form["fur"]
        energy = request.form["energy"]
        voice = request.form["voice"]
        maintenance = request.form["maintenance"]

        print(place, creature, fur, energy, voice, maintenance)

    
    return render_template('index.html')


@app.route('/sing_up', methods=['GET', 'POST'])
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



app.run(debug=True)







