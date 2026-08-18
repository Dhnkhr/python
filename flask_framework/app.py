from flask import Flask

app = Flask(__name__)  ### create an instance of flask class, wsgi

@app.route("/")
def welcome():
    return "welcome to the mahfill"

if __name__=="__main__":
    app.run(debug=True)