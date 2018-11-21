from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

@app.route("/")
def formpage():
    return render_template('formpage.html')

@app.route("/submit")
def submitpage():
    txtvalue = request.form['txtname']
    print("received:" + txtvalue)
    return "<h1>Thank you for </h1>"

if __name__=="__main__":
   app.run()