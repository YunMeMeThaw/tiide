from flask import Flask

app = Flask(__name__)

@app.route("/")
def Yun():
    return "Hello World"

@app.route("/Yun")
def tiide():
    return "Welcome to Yun Me Me Thaw"
