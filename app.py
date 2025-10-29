from flask import Flask, jsonify
import random

app = Flask(__name__)
quotes = [
    "La persévérance est la clé du succès.",
    "Chaque jour est une nouvelle opportunité.",
    "Apprends du passé, vis le présent."
]

@app.route('/quote')
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
