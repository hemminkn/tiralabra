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
key = input("Choose key, minors/majors: ")
degree = int(input("Choose degree: "))

if key == "minors":
    m = MarkovChain("Minors", degree)
if key == "majors":
    m = MarkovChain("Majors", degree)
else:
    print("Try again")
    pass

m.train()
file = generate(m.trie)

print("Midi-file is ready!")

if __name__ == "__main__":
    app.run(debug=True)
