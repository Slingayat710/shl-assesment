from flask import Flask, request, jsonify
from recommendation_engine import recommend_assessments  # Assuming this file exists

api = Flask(__name__)

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@api.route('/recommend', methods=['POST'])
def get_assessment_recommendations():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    recommendations = recommend_assessments(query)
    return jsonify({"recommended_assessments": recommendations})

if __name__ == '__main__':
    api.run(debug=True, port=5000)