import json
import re  #  For cleaning queries (optional)

def load_assessments(filepath="data/assessments.json"):
    """Loads assessment data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  #  Specify encoding
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please create this file with assessment data.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. Please check the file format.")
        return []

def clean_query(query):
    """(Optional) Cleans the query by removing irrelevant characters."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', query).lower()

def recommend_assessments(query):
    """
    Recommends assessments based on the query.
    (Replace the basic logic with your advanced method)
    """

    assessments = load_assessments()
    if not assessments:
        return []

    query = clean_query(query)  #  Optional: Clean the query
    query_words = query.split()
    recommended = []

    for assessment in assessments:
        name = assessment.get("Assessment name", "").lower()
        description = assessment.get("description", "").lower()
        test_type = [t.lower() for t in assessment.get("Test type", [])]

        if any(word in name or word in description or word in ' '.join(test_type) for word in query_words):
            recommended.append({
                "url": assessment.get("URL"),  #  Ensure you return a dictionary with "url"
                "Assessment name": assessment.get("Assessment name"),
                "Remote Testing Support": assessment.get("Remote Testing Support"),
                "Adaptive/IRT Support": assessment.get("Adaptive/IRT Support"),
                "Duration": assessment.get("Duration"),
                "Test type": assessment.get("Test type"),
            })
        if len(recommended) >= 10:
            break  #  Limit to 10 recommendations

    return recommended  #  Return the list of dictionaries

if __name__ == '__main__':
    #  Example Usage (for testing)
    test_query = "Java and SQL skills"
    recommendations = recommend_assessments(test_query)
    print(f"Recommendations for: {test_query}")
    for rec in recommendations:
        print(f"  - {rec['Assessment name']}: {rec['url']}")