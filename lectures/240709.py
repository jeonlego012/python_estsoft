# 버전의 중요성
from gtts import gTTS
from playsound import playsound

txt = '안녕하세요'
tts = gTTS(text=txt, lang='ko')
# tts.save(r"text.mp3")
playsound(r"text.mp3")

# 웹에서 데이터 추출
import webbrowser
import requests
import time

webbrowser.open('https://naver.com/robots.txt')  # SEO 검색 엔진 최적화. robots.txt 국제표준으로 모든 사이트에서 제공
webbrowser.open_new('https://google.com')
webbrowser.open_new_tab('https://daum.net')

r = requests.get('https://naver.com')
print(hash(r.text[4000:5000]))  # 웹 페이지 내용 바꼈나 비교 -> hash 값 비교
# 취약점 사이트 갱신 여부를 주기적으로 확인. 스레드로
while 1:
    r = requests.get('https://naver.com')
    print(hash(r.text))
    time.sleep(3)

# 사이트에서 특정 글자 찾기
start_num = r.text.find('날씨')
print(r.text[start_num:start_num+500])

# DB에 저장
# HeidiSQL로 mydatabase 라는 이름의 db를 생성하고 tbl_site_status_info 라는 테이블 만들기
# 1. url 5개 구성
# 2. http get
# 3. 3초마다 5개의 사이트에서 hash를 구하고
# 4. MariaDB의 테이블 tbl_site_status_info에 기록
import mysql.connector as db_connector

host = '223.130.143.157'
database_name = 'mydatabase'
user = 'lego'
pwd = 'legolego'

db_con = db_connector.connect(
    host=host,
    database=database_name,
    user=user,
    passwd=pwd,
)
db_cursor = db_con.cursor()

query = 'INSERT INTO tbl_site_status_info (url, hash) VALUES(%s, %s)'

urls = ['https://m.naver.com',
        'https://m.daum.net',
        'https://google.com',
        'https://perplexity.ai',
        'https://tistory.com']

while 1:
    for url in urls:
        r = requests.get(url)
        val = (url, hash(r.text))
        db_cursor.execute(query, val)
        db_con.commit()
    time.sleep(3)

db_con.disconnect()


# Quiz1
# 1) sqlite 혹은 mariadb상에  데이터베이스 이름으로 temp.db 를 만들고
# select sqlite_version() 쿼리하여 sqlite 혹은 mariadb의 데이터베이스 버전 정보를 얻는 코드를 작성해보시오
import mysql.connector as db_connector

db_con = db_connector.connect(
    host='223.130.143.157',
    user='lego',
    passwd='legolego'
)

print(db_con.is_connected())

db_cursor = db_con.cursor()

query = 'CREATE DATABASE IF NOT EXISTS temp'
db_cursor.execute(query)

query = 'select version()'
db_cursor.execute(query)
print(db_cursor.fetchall())

# 2) sqlite 혹은 mariadb상에 데이터베이스에 agent 라는 테이블을 만들고
# 각각의 컬럼을 다음과 같이 생성하는 코드를 작성해보시오
# agent_code char(6)
# agent_name char(40)
# working_area char(35)
# commission decimal(10,2)
# phone_no char(15) NULL
query = 'use temp'
db_cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS tbl_agent(agent_code CHAR(6), agent_name CHAR(40), working_area CHAR(35), commision DECIMAL(10,2), phone_no CHAR(15) NULL)'
db_cursor.execute(query)
db_con.commit()

# 3) SELECT name FROM sqlite_master WHERE type='table';
# 쿼리를 이용하여 2번에서 만든 테이블 정보를 얻는 코드를 작성하시오

query = "SELECT COLUMN_NAME, COLUMN_TYPE FROM information_schema.COLUMNS WHERE TABLE_NAME='tbl_agent'"
db_cursor.execute(query)
print(db_cursor.fetchall())


# 4) sqlite 혹은 mariadb상에 데이터베이스 이름으로 mysqlite.db를 생성하고 테이블과 컬럼을 생성한 다음, 아래의 쿼리를 동작시키고 이를 출력하는 코드를 작성하시오
# INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
# INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
# INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
# INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
# INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);

query = 'CREATE DATABASE IF NOT EXISTS mysqlite'
db_cursor.execute(query)

query = 'use mysqlite'
db_cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS tbl_salesman(code CHAR(6), name CHAR(40), working_area CHAR(35), commision DECIMAL(10,2))'
db_cursor.execute(query)

values = [(5001, 'James Hoog', 'New York', 0.15), (5002, 'Nail Knite', 'Paris', 0.25),
          (5003, 'Pit Alex', 'London', 0.15), (5004, 'Mc Lyon', 'Paris', 0.35), (5005, 'Paul Adam', 'Rome', 0.45)]
for value in values:
    query = f'INSERT INTO tbl_salesman VALUES{value}'
    db_cursor.execute(query)
    db_con.commit()

query = 'SELECT * FROM tbl_salesman'
db_cursor.execute(query)
print(db_cursor.fetchall())

db_con.disconnect()


# 5) sqlite 혹은 mariadb상에 데이터베이스 파이썬 코드중 일부 코드를 아래와 같이 예로 구성하였다.
# rows = [(5001,'James Hoog', 'New York', 0.15), (5002,'Nail Knite', 'Paris', 0.25),
# (5003,'Pit Alex', 'London', 0.15), (5004,'Mc Lyon', 'Paris', 0.35), (5005,'Paul Adam', 'Rome', 0.45)]
# 해당 코드 값이 적용되도록 임의의 데이터베이스를 생성하고 rows 내용이 적용되는 컬럼를 생성하여 rows 값을
# sql_connection() 와 sql_table() 를 활용하여 적용되는 코드를 작성하시오


def sql_connection():
    conn = db_connector.connect(
        host='223.130.143.157',
        user='lego',
        passwd='legolego',
        database='mysqlite'
    )
    if conn.is_connected:
        return conn


def sql_table(conn):
    cursor = conn.cursor()
    query = 'CREATE TABLE IF NOT EXISTS tbl_salesman(code CHAR(6), name CHAR(40), working_area CHAR(35), commision DECIMAL(10,2))'
    cursor.execute(query)
    conn.commit()


db_con = sql_connection()
sql_table(db_con)

rows = [(5001, 'James Hoog', 'New York', 0.15), (5002, 'Nail Knite', 'Paris', 0.25),
        (5003, 'Pit Alex', 'London', 0.15), (5004, 'Mc Lyon', 'Paris', 0.35), (5005, 'Paul Adam', 'Rome', 0.45)]

query = 'INSERT INTO tbl_salesman VALUES (%s, %s, %s, %s)'

db_cursor = db_con.cursor()
db_cursor = db_con.cursor()
db_cursor.executemany(query, rows)
db_con.commit()

query = 'SELECT * FROM tbl_salesman'
db_cursor.execute(query)
rows = db_cursor.fetchall()

for row in rows:
    print(row)

db_con.close()
