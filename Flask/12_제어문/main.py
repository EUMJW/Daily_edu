from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():

    list1= [10,20,30,40,50]

    return render_template('index.html', a1=10, a2=list1)

app.run(host='192.168.1.4',port=80,debug=True)