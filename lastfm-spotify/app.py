from flask import Flask, render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/name/<user>')
def hello_user(user):
    return render_template("index.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
