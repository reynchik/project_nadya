from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/about')
def about():
    
    return render_template('index.html')
app.run(debug=True)