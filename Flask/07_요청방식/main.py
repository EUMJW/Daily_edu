from flask import Flask,render_template, request

app=Flask(__name__)


# 요청 방식
# 브라우저가 서버에 요청 할 때 사용하는 방식
# get : post가 아니면 get방식
#       직접 주소를 입력한 경우,
#       링크를 클릭한 경우,
#       form 태그의 method가 get으로 설정되어 있는 경우 등등
# post : form태그의 method가 post로 설정되어 있는 경우

# Flask에서는 get방식, post방식을 구분해서 처리할 수 있다.

@app.route('/')
def index():
    return render_template('index.html')

# methods : 허용할 요청 방식을 지정한다. 생략시 get으로 지정된다.
@app.route('/test1', methods=['get'])
def test1():
    # request를 사용하면 브라우저가 전달한 요청 정보를 추출할 수 있다.
    # 이를 이용해 요청 방식을 파악할 수 있다.
    str1 = f'test - 요청방식 : {request.method}'
    return str1

@app.route('/test2', methods=['post'])
def test2():
    str1 = f'test2 - 요청방식 : {request.method}'
    return str1

# 같은 요청에 대해 get, post이 각각 다르게 처리해야 한다면 함수를 따로 등록해 준다.
@app.route('/test3', methods=['get'])
def test3_get():
    str1 = f'test3 - 요청방식 : get'
    return str1

@app.route('/test3', methods=['post'])
def test3_post():
    str1 = f'test3 - 요청방식 : post'
    return str1


# 만약 같은 요청에 대해 get/post가 똑같은 처리를 한다면 모두 받아들일 수 있게 설정한다.
@app.route('/test4', methods=['get','post'])
def test4():
    str1 = f'test4 - 요청방식 : {request.method}'
    return str1

app.run(host='192.168.1.4', port=80, debug=True)