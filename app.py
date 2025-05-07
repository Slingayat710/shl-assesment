from flask import Flask, render_template, request
from recommendation_engine import recommend_assessments  # Assuming this file exists
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    query = request.form['query']
    recommendations = recommend_assessments(query)
    return render_template('results.html', query=query, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)