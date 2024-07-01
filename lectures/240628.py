# 숫자, 문자열 입력과 출력
# 십진수 -> 이진수
# 날짜 UTC

"""
binary = bin(10)
octal = oct(17)
hexadecimal = hex(25)
print(binary, octal, hexadecimal)
print(ord('a'))  # character -> number
print(chr(97))  # number -> character

list1 = range(0, 10)
list2 = list(range(0, 10))

print(list1)
print(list2)
print(sum(list1))
print(sum(list1, start=2))  # start : 더해줄 숫자

print(True)
print(True + True)
print(True & True)
print(True | True)
print(True ^ True)
print(True + False)
print(True & False)
print(True | False)
print(True ^ False)
print(not True)

a = hex(17)
if a == 0x11:
    print(True)
if a != 0x12:
    print(False)

print(pow(2, 4, 5))
print(divmod(2**4, 5))
print(16//5)
print(16 % 5)
print(divmod(16, 5))

print(min(2, 3, 4))
print(max(2, 3, 4))
print(min(list1))
print(max(list2))

fl1 = 10.12345678901234567890
fl2 = 10.98765432109876543210

print(float(fl1))  # 다 표현 안 됨
print(fl2)
print(fl1 + fl2)


# 복소수(complex)
# 실수와 가상의 수가 연결된 복잡한 수
print(type(3.14 + 4j))

# math 함수
import math

print(math.trunc(3.14))
print(math.trunc(fl2))

print(math.pi)

print(math.ceil(3.14))
print(math.trunc(3.14))
print(math.floor(3.14))
print(abs(-345))
print(math.fabs(-345))
print(round(3.456))
print(round(3.456, 1))
print(round(3.456, 2))
print(round(153.678, -1))

# printf 표현 방식
# escape sequence
str1 = '123'
str2 = 'ab'
str3 = 'abc'
print(" %s\t%s  \r" % (str1, str2), " and\n%.50f" % fl1)  # 쓰레기 값 추가
print("{}{}{}{a}".format(10, 12, 13, a=2))
print("{1}{0}{2}".format(1, 2, 3))

# Quiz1
print(type(4-68.7e100))

from numbers import Number
from decimal import Decimal
from fractions import Fraction
print(isinstance(2.0, Number),isinstance(Decimal('2.0'), Number),isinstance(Fraction(2, 1), Number),isinstance("2", Number),)

print((1.1 + 2.2) == 3.3)
print(round(100.2563, 3), round(100.000056, 3))
"""


# 문자열
'''
str1 = "python is powerful"
print(str1.capitalize())

print(str1.count('p', 3))  # [3:]
print(str1[3:].count('p'))
print(str1.find('p'))
print(str1.find('p', 9))

print('가'.encode('cp949'))  # b: binary
print('가'.encode('utf-8'))  #
print('가나다'.encode('utf-8'))  # 3byte
print(len('가나다'.encode('utf-8')))
print(b'\xea\xb0\x80'.decode(encoding='utf-8'))
print(b'\xb0\xa1'.decode(encoding='cp949'))

str2 = "python\tis\tpowerful"
print(str2.expandtabs(8))

str3 = '123abc'
if str3.isdigit():
    print('숫자임')
elif str3.isalpha():
    print('알파벳임')
elif str3.isalnum():
    print('알파벳과 숫자 중 하나라도 포함됨')
else:
    print('숫자 아님')

# isnumeric(), isdecimal(), isupper(), islower()
# isspace(), istitle()

print('Y'.isupper())
print('python'.upper())
print('Python is Powerful'.istitle())
print('python is powerful'.title())
'''

# Quiz2
'''
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]
print(stringList[1] == myString, stringList[1] is myString)


print(chr(97))
print(ord('c'))
print(ascii('c'))

str1 = str("pynative")
str2 = "pynative"
print(str1 == str2, str1 is str2)


print("John" > "Jhon", "Emma" < "Emm")

str1 = "my isname isisis jameis isis bond"
sub = "is"

print(str1.count(sub, 4))

print(id(sub))
sub = sub + "aaaa"  # 새로운 메모리 공간에 다시 할당됨. immutable
print(id(sub))
'''

# 파일 입출력
# r(read) w(write) a(append) + b(binary) t(text)
'''
f = open('test.txt', 'a')  # 파일 열기. f: 텍스트를 다룰 수 있는 객체
#data = f.read()  # 파일 읽기
f.seek(0)
f.write('first')

value = input()
print(value)

f.write(value)

f.close()  # 파일 닫기
'''

# Quiz3
x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))

print('%x, %X' % (15, 15))

# print('Ben', 25, 'California', sep='-')
# v = input()
# print(type(v))

print('[%c]' % 65)

sampleList = [5, 10, 15, 25]
print(sampleList[::-2])
del sampleList[0:6]
print(sampleList)

resList = [ x + y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)
sampleList.pop(2)
print(sampleList)

aList = ['a', 'b', 'c', 'd']
newList = aList.copy()
print(newList)
newList[1] = 'apple'
print(newList)