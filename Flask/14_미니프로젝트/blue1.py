# blue1.py

from flask import Blueprint, render_template, request
from db import db_connect

# BluePrint 객체를 생성한다.
# 첫 번째 : blueprint의 이름
# 두 번째 : blueprint를 관리할 Flask 객체의 이름
topic_blue = Blueprint('topic_blue', __name__, template_folder='topic_template')

@topic_blue.route('/test1')
def test1() :
    return render_template('test1.html')

# 토론방 메인
@topic_blue.route('/topic_main')
def topic_main() :
    # 데이터베이스 접속
    conn = db_connect()
    # 방번호, 토론 주제 가져오기
    sql = '''
            select a2.topic_idx, a2.topic_subject , a1.cnt
            from topic_table a2
             left join(select content_topic_idx, count(*) as cnt
                                from content_table
                                group by content_topic_idx
                                order by content_topic_idx desc ) a1
            on a2.topic_idx = a1.content_topic_idx
            order by topic_idx desc
          '''

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    # # 각 방별 글 개수를 가져온다.
    # sql2 = '''
    #         select content_topic_idx, count(*)
    #         from content_table
    #         group by content_topic_idx
    #         order by content_topic_idx desc
    #        '''
    #
    # cursor2 = conn.cursor()
    # cursor2.execute(sql2)
    # result2 = cursor2.fetchall()
    #
    # print(result)
    # print(result2)
    conn.close()

    return render_template('topic_list.html', topic_list=result)

# 토론방 추가
@topic_blue.route('/add_topic')
def add_topic() :
    return render_template('add_topic.html')

# 토론방 추가 처리
@topic_blue.route('/add_topic_pro', methods=['post'])
def add_topic_pro() :
    # 파라미터 데이터 추출
    topic_name = request.values.get('topic_name')

    # db 접속
    conn = db_connect()

    sql = '''
            insert into topic_table (topic_subject)
            values (?)
          '''

    data = [topic_name]
    conn.execute(sql, data)
    conn.commit()
    conn.close()

    return '''
            <script>
                alert('저장되었습니다')
                location.href = '/topic_main'
            </script>
           '''




