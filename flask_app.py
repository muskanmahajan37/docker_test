from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":

    # run the app locally on the given port
    app.run(host='0.0.0.0', port=8000)
# optional if we want to run in debugging mode