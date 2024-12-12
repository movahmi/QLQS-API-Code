from flask import Flask, request, jsonify
import numpy as np
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Dummy Database (Replace with real data source later)
database = [
    {"id": 1, "name": "Item A", "description": "This is item A."},
    {"id": 2, "name": "Item B", "description": "Another item B."},
    {"id": 3, "name": "Item C", "description": "Description of C."},
    {"id": 4, "name": "Item D", "description": "Item D is here."},
    {"id": 5, "name": "Item E", "description": "Last item in the list."}
]

# Quantum-Inspired Search Simulation Function
def quantum_search_simulation(query, data):
    """
    A very simple simulation of quantum-inspired search.
    It doesn't use actual quantum physics, but mimics the idea
    of searching multiple possibilities simultaneously.
    """
    logging.info(f"Starting search for query: {query}")
    results = []
    for item in data:
        if query.lower() in item['name'].lower() or query.lower() in item['description'].lower():
            results.append(item)
    logging.info(f"Found {len(results)} matching items.")
    return results

# API Endpoint
@app.route('/search', methods=['GET'])
def search_items():
    query = request.args.get('q')
    if not query:
        logging.warning("Query parameter 'q' is missing.")
        return jsonify({"error": "Please provide a query parameter 'q'"}), 400

    results = quantum_search_simulation(query, database)
    return jsonify(results)


if __name__ == '__main__':
    logging.info("Starting the Flask API...")
    app.run(debug=True)  # debug=True for development only