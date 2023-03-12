from flask import Flask
from flask_cors import CORS
from graph import Graph

app = Flask("__name__")
CORS(app)

@app.route("/")
def start() -> dict:
    return {"home_string": "Synonyms search tool"}

@app.route("/get/<word>")
def get_synonyms(word: str) -> dict:
    return {word: graph.get_synonyms(word)}

@app.route("/add/<word>/<synonymsInput>")
def add_word(word: str, synonymsInput: str) -> dict:
    synonyms = synonymsInput.split(",")

    graph.add_word(word, synonyms)
    return {word: graph.get_synonyms(word)}

if __name__ == "__main__":
    graph = Graph()
    app.run(debug=True)