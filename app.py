from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/dashboard")
#def dashboard():
#  return render_template("dashboard.html")


@app.route("/login")
def hello_world():
  return render_template("dashboard.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
