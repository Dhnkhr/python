from flask import Flask, render_template,request

app = Flask(__name__)  ### create an instance of flask class, wsgi

@app.route("/")
def welcome():
    return "<html><H1>welcome to the Mefill</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    if score >=50 :
       res="passed"
    else:
       res="failed"
    return render_template('result.html',result=res)

if __name__=="__main__":
    app.run(debug=True)