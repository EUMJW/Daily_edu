# 모듈
from flask import Flask

# 서버를 생성한다.
# flask 객체를 생성하면 서버가 생성되고
# 이를 이용해 서버를 가동하면 된다.
# Flask 객체를 만들때 문자열 아무거나 넣어주면 된다. 보통 __name__

app = Flask(__name__)

# 브라우저 요청 정보에 따라 처리하는 부분
# return이 브라우저로 전달

# 주소만 입력했을때
@app.route("/")
def index() :
    return 'Hello World'

# 주소 뒤에 test를 붙였을때
@app.route('/test')
def test() :
    return 'Hello Test'


# 서버가동
# host : 브라우저가 요청할때 사용할 ip 주소
# 현재 서버역활을 할 컴퓨터의 ip주소
# port : 브라우저가 사용할 포트 번호
# 포트번호는 컴퓨터에서 프로그램을 구분하기 위한 수단
# debug : True 를 넣어주면 파일 수정시 서버가 자동으로 가동
# 개발시에만 설정

app.run(host='192.168.1.4', port='80', debug=True)

