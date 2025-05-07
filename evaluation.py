from flask import Flask, render_template, request
from recommendation_engine import recommend_assessments
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    query = request.form['query']
    recommendations = recommend_assessments(query)
    return render_template('results.html', query=query, recommendations=recommendations)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)