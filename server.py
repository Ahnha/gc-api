from flask import Flask, request, jsonify
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)
CORS(app, origins=["https://ahnha.github.io"])  # allow specific origin

# Define a route for our GC content calculation API
@app.route("/gc-content", methods=["POST"])
def gc_content():
    data = request.get_json()  # Read JSON body
    sequence = data.get("sequence", "")  # Extract the sequence string

    # Calculate GC content
    if sequence:
        gc_count = sequence.upper().count("G") + sequence.upper().count("C")
        gc_percent = (gc_count / len(sequence)) * 100
    else:
        gc_percent = 0

    # Return JSON response
    return jsonify({"gc_content": gc_percent})

# Start the app on localhost:8080
if __name__ == "__main__":
 app.run(host="127.0.0.1", port=8080)

