from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome! </p> <a href=http://127.0.0.1:5000/hello> Hello </a></p><a href=http://127.0.0.1:5000/goodbye> Goodbye </a>"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

if __name__=="__main__":
   app.run()