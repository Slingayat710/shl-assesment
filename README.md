# SHL Assessment Recommendation System

## Overview

This project implements an intelligent assessment recommendation system as per the requirements of the SHL AI Intern RE Generative AI assignment. [cite: 3, 4] The system takes a natural language query or job description and returns a list of relevant SHL assessments from the provided catalog. [cite: 1, 2, 5]

## Features

- **Web Application:** A user-friendly interface for entering queries and viewing assessment recommendations. [cite: 1, 2, 3, 4]
- **API Endpoint:** An API that accepts queries and returns assessment recommendations in JSON format.
- **Assessment Recommendations:** Provides a list of relevant SHL assessments with key attributes. [cite: 5]
- **Evaluation Metrics:** Calculates Mean Recall@K and MAP@K to evaluate the system's performance.

## Technologies Used

- Python (version x.x)
- Flask (for the web application and API)
- JSON

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Slingayat710/shl-assesment.git
    cd shl-assesment
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    _(Note: Create a `requirements.txt` with `flask`.)_

3.  **Run the application:**

    - **To start the web application:**

      ```bash
      python app.py
      ```

      - Accessible at `http://127.0.0.1:5000/`.

    - **To start the API:**

      ```bash
      python api.py
      ```

      - Accessible at `http://127.0.0.1:5001/`.

## API Usage

- **POST /recommend:** Accepts a JSON payload `{"query": "your text"}` and returns a JSON list of recommended assessments with "url", "remote_support", "adaptive_support", "duration", and "test_type".

## Evaluation

- Run `python evaluation.py` to calculate Mean Recall@K and MAP@K using `test_queries.json`.

## Recommendation Algorithm

- The system uses a basic keyword matching approach. The query is tokenized, and assessments in `assessments.json` are checked for the presence of these tokens in their "Assessment name" and "Test type". More sophisticated NLP or LLM-based methods could improve accuracy.

## Design Choices

- Flask was chosen for its simplicity and ease of use in building web applications and APIs in Python. Assessment data is stored and accessed from the `assessments.json` file.

## Challenges and Solutions

- A challenge was accurately mapping natural language queries to specific assessment types. A more advanced NLP model would be a better solution than simple keyword matching.
