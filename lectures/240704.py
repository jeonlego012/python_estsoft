# mission1) 임의의 클래스 A와 B를 B클래스에서 A를 상속하여 다음과 같은 결과를 출력하시오
# BInst = B("test", 100, True)

class A:
    def __init__(self, x, y, z):
        self.string = x
        self.integer = y
        self.boolean = z


class B(A):
    def result(self):
        print(self.string, self.integer, self.boolean)


BInst = B("test", 100, True)
BInst.result()


# mission2) 리스트와 세트로 구성되어 있는 구조를 모두 세트 형태로 출력하시오(출력 순서 무관)
# 출력: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
for sample in sample_list:
    sample_set.add(sample)
print(sample_set)


# mission3) 두개의 set 값에서 중복된 값만 뽑아 출력하시오 (intersection 함수 활용)
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))


# mission4) 두개의 set 값에서 중복을 제거하여 set를 결합하고 출력하시오 (union 함수 활용)
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))


# mission5) difference_update 를 이용하여 set1의 값 중에 set2에 존재하는 값을 제거한 다음 출력하시오.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)


# mission6) 두 개의 set에서 중복된 값을 찾아 출력하시오 (isdisjoint 함수 활용)
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("no duplicate")
else:
    print(set1.intersection(set2))


# mission7) 주어진 튜플을 reverse로 출력하시오.
tuple1 = (10, 20, 30, 40, 50)
print(tuple(reversed(tuple1)))
###
print(tuple1[::-1])

# mission8) 주어진 튜플에서 30만 출력하시오.
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple2[1][2])


# mission9) swap하는 함수를 만들거나 변수 스왑을 하시오.
def swap(a, b):
    c = a
    a = b
    b = c
    print(f"after) a: {a}, b: {b}")


tuple1 = (11, 22)
tuple2 = (99, 88)
print(f"before) a: {tuple1}, b: {tuple2}")
swap(tuple1, tuple2)
####
tuple1 = (11, 22)
tuple2 = (99, 88)
print(f"before) a: {tuple1}, b: {tuple2}")
tuple1, tuple2 = tuple2, tuple1
print(f"after) a: {tuple1}, b: {tuple2}")


# mission 10) tuple1 = (11, [22, 33], 44, 55) 에서 tuple1: (11, [222, 33], 44, 55) 로 출력하시오.
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# mission 11) tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29)) 값을 sort 하여
# (('c', 11), ('a', 23), ('d', 29), ('b', 37)) 로 출력하시오
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(tuple1, key=lambda value: value[1]))
print(tuple1)


# mission 12) tuple 의 값이 모두 같다면 True 그렇지 않으면 False를 반환하는 함수를 만드시오
# all 함수. 반복 개체의 모든 요소가 True인지
def is_same(iterable):
    return all(iterable[0] == element for element in iterable)


tuple1 = (45, 45, 45, 45)
tuple2 = (45, 45, 45, 44)
print(is_same(tuple1))
print(is_same(tuple2))
print(is_same([11, 11, 11]))


# ftp
from ftplib import FTP
ftp = FTP("ftp.kaist.ac.kr")
ftp.login()
ftp.retrlines('LIST')
ftp.quit()


# DB I/O
import mysql.connector as db_connector

host = '223.130.143.157'
database_name = 'python_db_test'
user = 'lego'
pwd = 'legolego'

db_con = db_connector.connect(
    host=host,
    database=database_name,
    user=user,
    passwd=pwd
)

print(db_con.is_connected())

db_cursor = db_con.cursor()

query = 'TRUNCATE TABLE tbl_usr'
db_cursor.execute(query)

_id = 'lego'
_pwd = 'legopwd'
_name = 'jeonlego'
_phone = '010-1234-1234'
val = (_id, _pwd, _name, _phone)
query = 'INSERT INTO tbl_usr (id, pwd, name, phone) VALUES(%s, %s, %s, %s)'
db_cursor.execute(query, val)
db_con.commit()

query = 'SELECT * FROM tbl_usr'
db_cursor.execute(query)
result_set = db_cursor.fetchall()  # return set
print(result_set)


db_con.disconnect()


# Quiz1
# 1) 5자리 이상 영문으로 된 id 를 1000개 임의 생성하는 코드를 작성해보세요
import random
import string


en_id_list = []
for i in range(1000):
    digit = random.randint(5, 10)
    random_id = "".join(random.choice(string.ascii_lowercase) for c in range(digit))
    en_id_list.append(random_id)
print(en_id_list)


# 2) 랜덤함수를 활용하여 다음 처럼 이름, 휴대폰 번호, id 를 가상으로 생성하는 코드를 작성해보세요 (1000개 정도의 임의 생성 필요)

# 이름 생성
last_name_list = [
    "가", "간", "갈", "감", "강", "경", "계", "고", "공", "곽", "구", "국", "권", "금", "기", "길", "김", "나", "남", "남궁", "노", "도", "독고",
    "류", "마", "문", "박", "방", "배", "백", "봉", "사공", "서", "선우", "설", "성", "손", "송", "신", "심", "안", "양", "엄", "여", "영", "예", "오",
    "옥", "왕", "우", "원", "위", "유", "윤", "이", "임", "장", "전", "정", "제", "제갈", "조", "좌", "주", "지", "진", "차", "채", "천", "최",
    "추", "쾌", "탁", "태", "팽", "편", "표", "피", "하", "한", "함", "허", "현", "호", "홍", "황", "황보"
]
first_name_list = [
    "가", "각", "간", "갇", "갈", "감", "갑", "갓", "강", "갱", "겐", "겸", "겹", "경", "계", "고", "곡", "곤", "곧", "골", "곰", "곱", "곳", "공", "곽", "관", "광", "교", "구", "국", "군", "굴", "굼", "굽", "규", "균", "귤", "그", "극", "글", "금", "긍", "기", "긱", "긴", "길", "김", "느", "담", "답", "다", "단", "달", "담", "당", "대", "더", "도", "독", "돈", "돌", "동", "두", "라", "러", "련", "령", "로", "록", "론", "류", "륜", "률", "름", "다", "리", "림", "말", "미", "민", "빈", "분", "비", "삼", "상", "서", "석", "선", "설", "성", "세", "소", "손", "솔", "솜", "송", "수", "순", "신", "실", "심", "아", "안", "알", "압", "얼", "엄", "연", "열", "엽", "영", "예", "오", "옥", "온", "완", "요", "용", "우", "욱", "운", "웅", "위", "유", "율", "응", "이", "익", "인", "일", "임", "자", "장", "재", "전", "절", "점", "정", "제", "조", "주", "죽", "준", "줄", "중", "지", "진", "자", "착", "찬", "체", "치", "친", "키", "파", "표", "피", "하", "학", "한", "할", "함", "합", "항", "해", "햄", "햇", "향", "허", "헌", "헐", "험", "협", "현", "형", "혜", "호", "혹", "혼", "홀", "홈", "홉", "화", "확", "환", "활", "황", "회", "휴", "흉", "흑", "흘", "힘", "히", "힌",
]


def create_name():
    name = random.choice(last_name_list) + "".join(random.choices(first_name_list, k=2))
    return name


# 휴대폰 번호 생성
def create_phone_number():
    phone_number = random.choices(range(10), k=8)
    phone_number = list(map(str, phone_number))
    phone_number = "".join(phone_number[:4]) + "-" + "".join(phone_number[4:])
    return "010-" + phone_number


# id 생성
alphabet_list = list(string.ascii_lowercase)
number_list = [n for n in range(10)]


def create_id(loop_count):
    user_id = random.choice(alphabet_list)  # 알파벳으로 시작
    for i in range(loop_count - 1):
        random_character = str(random.choice(alphabet_list + number_list))
        user_id += random_character
    return user_id


for i in range(3):
    digit = random.randint(4, 10)
    print(create_name(), create_phone_number(), create_id(digit))

# 3) 네이버클라우드에 생성한 vpc 인스턴스에 구성된 mariadb 서버에 임의의 데이터베이스를 생성하고 해당 데이터베이스에 tbl_usr_data 라는 테이블을 생성한 다음,
# no, id, pwd, name. phone 컬럼을 생성하고
# 랜덤함수를 활용하여 id ~ phone 까지 값 1000개 insert 하고 select 하여 db 에 저장된 값을 호출하는 코드를 파이썬으로 작성하시요
# no 는 unique 성질이므로, 값을 생성하지 않고 auto_increment 로 되어 있어야 합니다.
import mysql.connector as db_connector

host = '223.130.143.157'
database_name = 'python_db_test'
user = 'lego'
pwd = 'legolego'

db_con = db_connector.connect(
    host=host,
    database=database_name,
    user=user,
    passwd=pwd
)

print(db_con.is_connected())

db_cursor = db_con.cursor()

query = 'TRUNCATE TABLE tbl_usr_data'
db_cursor.execute(query)

for i in range(10):
    digit = random.randint(4, 10)
    _id = create_id(digit)
    digit = random.randint(4, 10)
    _passwd = create_id(digit)
    _name = create_name()
    _phone = create_phone_number()

    val = (_id, _passwd, _name, _phone)
    query = 'INSERT INTO tbl_usr_data (id, pwd, name, phone) VALUES(%s, %s, %s, %s)'
    db_cursor.execute(query, val)
    db_con.commit()

query = 'SELECT * FROM tbl_usr_data'
db_cursor.execute(query)
result_set = db_cursor.fetchall()
print(result_set)

db_con.disconnect()

