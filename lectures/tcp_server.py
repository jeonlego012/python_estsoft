# 연결한 다음에 응답을 기다림
# 10000 포트에 내 ip를 묶어줌 : binding
# 응답을 기다림 : listen

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 10000))
s.listen()


while True:
    con, addr = s.accept() # accept가 계속 이뤄져야함. client의 connect에 매핑되어야함. connect-accpet
    print(addr)  # 어떤 client가 접속을 했는지 출력
    data = con.recv(1024)
    print('From client: ' + str(data))
    con.send(b'Listening')
    if data == b'hello':
        break
    con.close()

s.close()
