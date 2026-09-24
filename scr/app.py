from markov_chain import MarkovChain
from generator import generate
from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Generator")

#testing
m = MarkovChain("Minors", 2)
m.train()
generate(m.trie)

if __name__ == "__main__":
    app.run(debug=True)
