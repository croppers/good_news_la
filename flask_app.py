from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

neighborhood_clusters = [
    "Brentwood, Palisades, Malibu",
    "Westwood",
    "Beverly Crest, Bel Air",
    "Santa Monica, Venice",
    "Playa Vista, Marina del Rey",
    "Rancho Park, Cheviot Hills, Sawtelle",
    "Beverly Hills, Century City",
    "Pico Robertson, Beverlywood",
    "Palms, Culver City, Ladera Heights"
]

@app.route('/')
def index():
    return render_template('index.html', neighborhoods=neighborhood_clusters)

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/random')
def random_page():
    random_neighborhood = random.choice(neighborhood_clusters)
    return redirect(url_for('neighborhood', name=random_neighborhood))

@app.route('/neighborhood/<name>')
def neighborhood(name):
    if name not in neighborhood_clusters:
        return "Neighborhood not found", 404
    return render_template('neighborhood.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
