from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home(vert = 8, hori = 8):
    return render_template("index.html", vert = vert, hoti = hori )

@app.route("/<int:vert>/<int:hori>") # i is height and j is length
def checker(vert, hori):
    return render_template("index.html", vert = vert, hori = hori)


if __name__ == "__main__":
    app.run(debug=True)