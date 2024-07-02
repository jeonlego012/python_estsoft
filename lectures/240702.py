# print() 함수에서 sep을 이용하여 "파이썬으로**다양한**수업**과제중입니다" 출력하시오.
print("파이썬으로", "다양한", "수업", "과제중입니다", sep="**")

# input() 함수를 이용하여 decimal을 octal로 나오도록 코딩하시오.
decimal = int(input())
print(oct(decimal))

# input() 으로 입력을 받아 split() 을 이용하여 다음과 같이 출력하시오.
# Text1: True
# Text2: False
# Text3: None

text1, text2, text3 = input().split()
print("Text1: %s\nText2: %s\nText3: %s" % (text1, text2, text3))


# input() 으로 리스트 형태로 입력받은 다음 float 값 여부를 확인하여 출력하시오.
num_list = input().split(",")
float_list = list()
for num in num_list:
    if "." in num:
        float_list.append(float(num))
print(float_list)


# sample.txt 에서 파일을 읽어 line6, line9번을 제외하고 출력해보세요
file = open("sample.txt")
line_list = file.readlines()
for line in line_list:
    index = line_list.index(line)
    if index != 5 and index != 8:
        print(line, end='')
file.close()

# 특정 파일에 내용이 비어있는지를 체크하는 코딩을 하시오.
import os
file_path = input("Enter path of file: ")
if os.path.getsize(file_path) > 0:
    print("%s is not empty" % file_path)
else:
    print("%s is empty" % file_path)


# 1********
# 12*******
# 123******
# 1234*****
# 12345****
# 123456***
# 1234567**
# 12345678*
# 123456789
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, end='')
    print("*" * (9 - i))


# 입력값이 10이면 1~10까지 모두 더해서 55를 출력하시오.
value = int(input())
value_sum = 0
for i in range(value+1):
    value_sum += i
print(value_sum)
print(sum(range(1, value+1)))

# 1~100 중에 짝수만 출력하시오.
x = 1
while x <= 100:
    if x % 2 == 0:
        print(x, end=' ')
    x += 1
print()
################
print([x for x in range(1, 101) if x % 2 == 0])
################
print([x for x in range(2, 101, 2)])
################
print(list(map(lambda x: x * 2, range(1, 50))))

# 리스트[10,72,120,170,145,525,50,40,10,25,177,200,325,40,32,155,333]의 값 중에 150보다 크고 400보다 작은 값을 출력하시오.
num_list = input().split(",")
print(type(num_list))
num_list = list(map(int, num_list))
print(list(filter(lambda num: 150 < num < 400, num_list)))


# 숫자가 입력되면 총 몇개의 숫자로 이루어진 것인지 출력하시오.
num = input()
print(len(num))
################
num = int(num)
digit = 0
while num > 0:
    num //= 10
    digit += 1
print(digit)


# 리스트의 값을 reversed() 를 반드시 활용하여 뒷쪽부터 출력해보시오.
num_list = [10, 72, 120, 170, 145, 525, 50, 40, 10, 25, 177, 200, 325, 40, 32, 155, 333]
print(*reversed(num_list))
num_list = list(reversed(num_list))
print(num_list)
# reversed() return object reversed
# list.reverse() execute reverse and return None
num_list.reverse()
print(num_list)


# input() 을 활용하여 숫자를 입력한 다음, 해당 숫자가 다 출력되고나서 "완료" 라는 메시지를 출력하시오.
num = int(input())
print(num, "\n완료")


# class
class ABC:
    num2 = 0

    def __init__(self):
        self.s1 = 'test'
        self._s2 = 'test2'
        self.__s3 = 'test3'  # 접근 불가
        self.__s3__ = 'test3__'
        self.num1 = 1234
        ABC.num2 = 5678

    def __del__(self):
        print('del')

    def f1(self, s2):
        self.s3 = 's3'
        return s2, self.s3


# 메모리 관점(할당-해제)
def func():
    func_abc = ABC()
    print(func_abc._s2, func_abc.__s3__, func_abc.num2)


abc = ABC()
func()

print(abc.f1('s2'))
print(abc.s1, abc.s3)


# Quiz1
aTuple = (10, 20, 30, 40, 50)
# aTuple.pop(2) -> AttributeError
print(aTuple * 2)

# tuple 선언
bTuple = 10, 20, 30
cTuple = (10,)
print(bTuple, cTuple)

dTuple = "Yellow", 20, "Red"
a, b, c = dTuple
print(a)

eTuple = ("Orange")
print(type(eTuple))

fTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(fTuple[1:2][0][1], fTuple[1][1])


# 문자와 숫자값을 넣고 출력되는 함수를 만드시오.
def print_string_number():
    s, num = input(), int(input())
    print(s, num)


print_string_number()


# 여러 개의 숫자가 인자로 들어가면 출력하는 함수를 만드시오.
def print_numbers(*numbers):
    print(numbers)


print_numbers(11, 20, 30, 445, 60, 191, 112)


# 여러 개의 숫자가 인자로 들어가면 해당 인자를 모두 더하는 함와 곱하는 함수를 각각 만드시오.
def sum_numbers(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number
    return sum_value


def multi_numbers(*numbers):
    multi_value = 1
    for number in numbers:
        multi_value *= number
    return multi_value


print(sum_numbers(1, 2, 3, 4, 5), multi_numbers(1, 2, 3, 4, 5))


# 입력한 숫자의 제곱근을 만드는 함수를 만드시오.
def square_root(number):
    return number ** 0.5


print(square_root(25))
################
import math
print(math.sqrt(25))


# 문자와 숫자 인자를 받아 출력하는 함수를 만든 동일한 동작을 하는 다른 이름의 함수를 만드시오.
def print_string_number(string, number):
    print(f"{string} {number}")


print_string_number('string', 2024)
print_string_number_copy = print_string_number
print_string_number_copy('string', 2025)


# 6에서 40까지의 숫자 값을 입력받고 짝수값만 나오는 코드를 한 줄로 작성하시오.
# list comprehension
print([x for x in range(6, 41) if x % 2 == 0])
# filter method
print(list(filter(lambda x: x % 2 == 0, range(6, 41))))
# range
print(list(range(6, 41, 2)))


# 주어진 수 중에 가장 큰 수와 가장 작은 수를 출력하시오.
def print_max_min(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    print(f"최댓값: {max_num}, 최솟값: {min_num}")


print_max_min([10, 72, 120, 170, 145, 525, 50, 40, 10, 25, 177, 200, 325, 40, 32, 155, 333])


# random
import os
import random
# seed, random, uniform, randrange, randint, gauss, choice, sample, shuffle

print(random.random())

print([random.randrange(20) for x in range(10)])
print(random.sample(range(20), 10))  # 중복 없이
print(random.sample(range(0, 30, 2), 4))
random.seed(6)
# random.seed(n) 무작위 결과를 특정한 시퀀스 값으로 고정. 난수 생성의 재현성 보장.
# 의사 난수 생성기(pseudo-random number generator) 초기화. 난수를 생성하기 위해 시드 값을 기본으로 사용하는데 시드 값이 제공되지 않으면 시스템의 현재 시간이 기본값.

s_list = [7, 15, 8, 52, 12, 53, 76, 90]
random.shuffle(s_list)
print(s_list)

c_list = [5, 11, 89, 34, 12, 65, 77, 10]
print(random.choice(c_list))


# Quiz2
import random
sampleList = [20, 40, 60, 80, 100, 120, 140, 160]
print(random.choice(sampleList))
print(random.sample(sampleList, 3))
print(random.choices(sampleList, weights=(10, 5, 15, 20, 50, 25, 30, 35), k=3))

print(random.uniform(20.5, 50.5))
print(random.randint(99, 200))  # end 포함
print(random.randrange(99, 200, 3))  # end 미포함

# 랜덤 생성기의 현재 상태를 저장(random.getstate())하고 복원(random.setstate(state))
random.seed(20)
state = random.getstate()
print(random.random())
print(random.random())

random.setstate(state)
print(random.random())
print(random.random())

random.setstate(state)
print(random.random())
print(random.random())


import uuid
print(uuid.uuid1())  # 네트워크 주소를 포함하여 고유 uuid 생성
print(uuid.uuid4())  # 무작위 고유 uuid 생성

import secrets
print(secrets.token_hex(32))  # 32바이트의 랜덤 보안 16진수 토큰 생성

print(secrets.randbelow(100))
print(random.SystemRandom().randint(100, 200))
