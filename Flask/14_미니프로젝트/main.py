# Flask : 서버 객체
# render_tamplate : html 파일을 통해 응답 결과를 생성하는 함수
# request : 사용자 요청 정보를 관리하는 객체
# Blueprint : 여러 파일로 나눠서 작업할 경우 사용하는 객체
# redirect : 자동으로 이동시킬 수 있는 함수
from flask import Flask, render_template, request, Blueprint, redirect
from blue1 import topic_blue
from blue2 import content_blue
from db import db_connect

app = Flask(__name__)

# blueprint 등록
app.register_blueprint(topic_blue)
app.register_blueprint(content_blue)

@app.route('/')
def index() :
    conn = db_connect()
    conn.close()
    # return render_template('index.html')
    # topic_main로 강제 이동시킨다.
    return redirect('/topic_main')

app.run(host='192.168.1.4', port=80, debug=True)

