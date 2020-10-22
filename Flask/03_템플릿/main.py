from flask import Flask, render_template

# app = Flask(__name__)
app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
    # return 'Hello World'
    # return '<h1>Hello World</h1>'
    # return '''
    #         <html>
    #             <head>
    #                 <meta charset='utf-8'/>
    #                 <title>test</title>
    #             </head>
    #             <body>
    #                 <h1>Hello World</h1>
    #                 <a href='http://google.com'>구글</a>
    #             </body>
    #         </html>'''
    # 지정된 템플릿 폴더안에 있는 html 파일을 처리해서 만들어진 html 코드를 브라우저로 전달한다.
    return render_template('index.html')


app.run(host='192.168.1.4', port=80, debug=True)

