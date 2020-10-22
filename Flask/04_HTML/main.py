from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



app.run(host='192.168.1.4', port=80, debug=True)
