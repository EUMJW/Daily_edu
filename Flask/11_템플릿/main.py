from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index() :
    # test1(100, 200, 300, 400, 500, 600, k1=700, k2=800, k3=900)
    # 지정된 html 파일을 가지고 데이터를 통해 유동적으로 HTML를 만들기 위해 사용하는 문법을 jinja2라고 부른다.

    dict1 = {'k1' : 100, 'k2' : 200}
    list1 = [10, 20, 30, 40, 50]

    return render_template('index.html', a1=100, a2=11.11, a3='안녕하세요', a4=dict1, a5=list1)

# 가변형 매개변수
# def test1(a1, a2, *a3, **a4) :
#     print(f'a1 : {a1}')
#     print(f'a2 : {a2}')
#     print(f'a3 : {a3}')
#     print(f'a4 : {a4}')


app.run(host='192.168.1.4',port=80,debug=True)