import os.path as osp

# 파일 시간 정보, 사이즈, 존재 여부,
osp.getatime("240627.py")  # access
osp.getmtime("240627.py")  # modify
osp.getctime("240627.py")  # create
osp.getsize("240627.py")
osp.isfile("240627.py")


# file database
import sqlite3
import os
con = sqlite3.connect("test.db")
# con.isolation_level = None  # commit 자동으로 해줌. transaction 격리하는 레벨.
cur = con.cursor()

# cur.execute("CREATE TABLE tbl_usr(id text, pwd text);")

# _id = 'testid'
# _pwd = 'testpwd'
# cur.execute("INSERT INTO tbl_usr VALUES(?, ?);", (_id, _pwd))
#
# seq_of_parameters = ((_id, _pwd), (_id, _pwd))
# cur.executemany("INSERT INTO tbl_usr VALUES(?, ?);", seq_of_parameters)


cur.execute("select * from tbl_usr;")

for row in cur:  # cur 메모리 내용을 pop
    print("row:", row)


# 여러번 쓸 경우
cur.execute("select * from tbl_usr;")
datas = cur.fetchall()  # cur 메모리 내용을 pop
print(cur.fetchall())

for row in datas:
    print("row:", row)
print(datas)

# stack push, pop (LIFO)
stack = []
stack.append("test1")  # push
stack.append("test2")
print(stack.pop())  # pop
print(stack)


# con.iterdump()  # DB 백업. SQL 뽑아내기
with con:
    with open("test_db_dump.sql", "w") as f:
        for i in con.iterdump():
            f.write(i+"\n")
        f.close()

os.startfile("test_db_dump.sql")
con.commit()  # transaction 적용
con.close()


# thread programming
# thread 선언(객체 생성)
# thread 시작
# 한 개의 프로세스에 여러 역할을 부여할 때 스레드가 필요
from threading import Thread, Lock
import time
import queue

lock = Lock()
q = queue.Queue()

q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(q.get())
print(q.qsize())
print(q.get())
print(q.get())


def test1(_title, _delay):
    count = 0
    while 1:
        # lock.acquire()  # thread1, thread2가 동시에 변수(count)에 접근하는 것을 막음. race condition 예방
        print(_title, ' put : ', count)
        q.put(count)
        # q.put_nowait(count)  # blocking 안 하고 빠져나옴. 필요에 따라
        count += 1
        # lock.release()
        time.sleep(_delay)

        if count > 10:
            break


def test2(_title, _delay):
    while 1:
        # lock.acquire()  # thread1, thread2가 동시에 변수(count)에 접근하는 것을 막음. race condition 예방
        count = q.get()
        # count = q.get_nowait()  # blocking 안 하고 빠져나옴. 필요에 따라
        print(_title, ' get :', count)
        # count += 1
        # lock.release()

        time.sleep(_delay)

        if count > 9:
            break


thread1 = Thread(target=test1, args=('thread1', 0.5))
thread2 = Thread(target=test2, args=('thread2', 0.6))
thread1.start()
thread2.start()

thread1.join()
thread2.join()


# Quiz
# {'key1': ['value1', 'value2'], 'key2': ['value3', 'value4', 'value5']}
# {'key1': ['value1', 'value2'], 'key2': ['value3', 'value4', 'value5']}

dict1 = {"key1": ['value1', 'value2'], 'key2': ['value3', 'value4', 'value5']}
print(dict1)
print(dict1)

import timeit
import random
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from __main__ import random, x")
    x = list(range(i))  # 리스트
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}  # 딕셔너리
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
