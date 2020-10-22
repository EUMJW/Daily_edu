# db.py

import sqlite3

# 데이터베이스 접속 함수
def db_connect() :
    conn = sqlite3.connect('topic.db')
    # sqlite 타입 : integer(정수), real(실수), text(문자열), date(날짜)
    sql1 = '''
            create table if not exists topic_table(
                topic_idx integer primary key autoincrement,
                topic_subject text not null
            );
          '''

    sql2 = '''
            create table if not exists content_table(
                content_idx integer primary key autoincrement,
                content_topic_idx integer not null,
                content_text text not null,
                foreign key(content_topic_idx) references topic_table(topic_idx)
            )
           '''

    conn.execute(sql1)
    conn.execute(sql2)

    conn.commit()

    return conn










