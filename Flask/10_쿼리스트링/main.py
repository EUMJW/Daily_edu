from flask import Flask, render_template, request

# 쿼리스트링 : 브라우저가 요청하는 주소에서 도메인과 파라미터 부분을 제외한 곳
# http://abc.com/a1/a2/a3?v1=100&v2=200
# => a1/a2/a3 부분

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/test1")
def test1() :
    return '<h1>test1</h1>'

@app.route('/test1/sub1')
def test1_sub1() :
    return '<h1>test1 sub1</h1>'

@app.route('/test1/sub2')
def test1_sub2() :
    return '<h1>test1 sub2</h1>'

# test2 다음으로 셋팅된 문자열은 주소가 아닌 데이터로 취급해서 str1 변수에
# 담길 수 있도록 설정한다.
# 만약 test2 다음에 나오는 값의 수가 다를 수 있고 처리하는 코드가 다르다면
# 각각 함수를 만들어 등록해준다.

# test2 다음에 값 하나가 설정되어 있을 경우 호출된다.
@app.route('/test2/<str1>')
def test2(str1) :
    return f'<h1>test2 : {str1}</h1>'
# test2 다음에 값이 없는 경우
@app.route('/test2')
def test22() :
    return f'<h1>test2</h1>'
# test2 다음에 값이 두개인경우
@app.route('/test2/<str1>/<str2>')
def test222(str1, str2) :
    return f'<h1>test2 : {str1}, {str2}</h1>'

# 서로다른 요청에 대해 같은 처리를 한다면 하나의 함수에 등록한다.
@app.route("/test3")
@app.route("/test4")
def test3_test4() :
    return f'<h1>test3 test4</h1>'

# 쿼리스트링의 개수가 다르더라도 같은 처리를 하겠다면 함수 하나에 셋팅한다.
@app.route("/test5", defaults={'str1' : 1, 'str2' : 2})
@app.route("/test5/<str1>", defaults={'str2' : 2})
@app.route("/test5/<str1>/<str2>")
def test5(str1, str2) :
    return f'''
            <h1>test5</h1>
            <h3>str1 : {str1}</h3>
            <h3>str2 : {str2}</h3>            
            '''

app.run(host='192.168.1.4', port=80, debug=True)