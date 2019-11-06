from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def indexku():
    nilaiku = 100
    return render_template("index.html", value=nilaiku)


if __name__ == "__main__":
    app.run(debug=True)
