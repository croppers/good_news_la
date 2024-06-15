from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

neighborhoods = [
    "Hollywood", "Downtown", "Beverly Hills", 
    "Santa Monica", "Venice", "Westwood", 
    "Silver Lake", "Echo Park", "Pasadena"
]

@app.route('/')
def index():
    return render_template('index.html', neighborhoods=neighborhoods)

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/random')
def random_page():
    random_neighborhood = random.choice(neighborhoods)
    return redirect(url_for('neighborhood', name=random_neighborhood))

@app.route('/neighborhood/<name>')
def neighborhood(name):
    if name not in neighborhoods:
        return "Neighborhood not found", 404
    return render_template('neighborhood.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
