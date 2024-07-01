# 문제
# 두 개의 정수가 주어지고 곱이 1000보다 작거나 같으면 곱을 반환합니다.
# 그렇지 않으면 합을 반환합니다.


def func(x, y):
    if x * y <= 1000:
        print(x * y)
    else:
        print(x + y)


num1, num2 = map(int, input().split())
func(num1, num2)

# 처음 10개의 숫자를 반복하는 프로그램을 작성하고, 각 반복마다 현재 숫자와 이전 숫자의 합을 출력합니다.


def sum_num(*numbers):
    print(*numbers)
    num_sum = 0
    prev_num = 0
    for number in numbers:
        num_sum = prev_num + number
        print("현재 번호", number, "이전 번호", prev_num, "합계:", num_sum)
        prev_num = number


sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# 입력받은 문자열에서 짝수 인덱스 번호에 있는 문자를 표시하시오.
string = input()

for char in string[0::2]:  # .index 함수는 같은 문자가 있을 때 제대로 출력 못 함
    print(char)


# 함수에 문자열을 넣고 인자로 n을 넣으면 n번째 이후 글자가 출력되도록 하시오


def print_char(string, n):
    print(string[n:])


print_char('Python', 2)


# 리스트를 만들고 첫번째 숫자와 마지막 숫자가 같아면 True, 다르면 False를 출력하시오
# 5로 나누었을 때 나누어 떨어지는 숫자를 표시하시오.


def list_func(num_list):
    print(num_list[0] == num_list[-1])

    for num in num_list:
        if num % 5 == 0:
            print(num)


list_func([10, 11, 12, 15, 18, 10])
list_func([20, 25, 33, 45, 54, 24, 2, 30])
list_func([5])

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5 출력
for i in range(6):
    for j in range(i):
        print(i, end=' ')
    print()


# Quiz1
set1 = {"Yellow", "Orange", "Black"}
# set1[1] -> Error
# set is unordered
set1.add("Blue")
set1.add("Orange")
print(set1)
set2 = {"Orange", "Blue", "Pink"}
set3 = set2.difference(set1)
print(set3)
set1.difference_update(set2)
print(set1)


# 집합은 immutable한 객체들로만 구성
# aSet = {1, "PYnative", ['abc', 'xyz'], True} -> Error
aSet = {1, "PYnative", ('abc', 'xyz'), True}

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set1.isdisjoint(set2))  # 서로소

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue")
print(sampleSet)

# set copy
set2 = set1.copy()
set2 = set(set1)
set2.update(set1)


# 입력값이 회문(palindrome)인지 아닌지를 확인하는 함수를 만들어 보시오


def palindrome(value):
    value = str(value)
    is_palindrome = True
    size = len(value)
    for i in range(0, size//2):
        is_palindrome = (value[i] == value[size-i-1])
        if not is_palindrome:
            break
    return is_palindrome


'''
def palindrome(value):
    value = str(value)
    return value == value[::-1]
'''

print(palindrome(119))
print(palindrome("1555521"))
print(palindrome("madam"))
print(palindrome("racecar"))
print(palindrome("apple"))

# list slicing (시작:끝:간격)
a = "IamJeonLego"
print(a[::2], a[1:7:2], a[::-1])

# list comprehension : 리스트 기반한 리스트 만들기
print([x for x in range(1, 10) if x % 2 == 0])
fruit_list = ['apple', 'banana', 'grape', 'watermelon']
print([x for x in fruit_list if len(x) > 5])


# 첫번째 리스트에서는 홀수값을, 두번째 리스트에서는 짝수값을 추출하여 새로운 리스트를 생성하고 출력하시오.

def merge_list(list1, list2):
    new_list = list()
    new_list.extend(a for a in list1 if a % 2 == 1)
    new_list.extend(b for b in list2 if b % 2 == 0)
    print(new_list)
    # filter: 리스트 원소 중 조건이 참인 원소들로 새로운 리스트 만들어줌
    new_list = list(filter(lambda a: a % 2 == 1, list1)) + list(filter(lambda b: b % 2 == 0, list2))
    print(new_list)


merge_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])


# 숫자로 입력된 값을 역순으로 출력하는 함수를 작성하시오

def reverse(number):
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number //= 10
    print(reversed_num)
    # convert to string
    # number = str(number)
    # number = int(number[::-1])
    # print(number)


reverse(123456)


# Quiz2
student = {
    "name": "Emma",
    "class": 9,
    "marks": 75,
}
print(student.get('marks'), student['marks'])

dict1 = {"key1": 1, "key2": 2}
dict2 = {"key2": 2, "key1": 1}
print(dict1 == dict2)

dict1 = {"name": "Mike", "jeon": "lego", "salary": 8000, "key": "value"}
print(dict1.get('age'))
# print(dict1.pop('age')) -> KeyError
# python 3.7 이후부터 dictionary 순서 유지
print(dict1.popitem())
print(dict1)


# 과세의 총 소득은 4500만원. 소득세를 계산해보시오.
# 과세소득          세율(%)
# 1000만원          0
# 1500만원          10
# 나머지            20


def calculate_tax(income):
    tax = 10000000*0 + 15000000*0.1 + (income - 25000000)*0.2
    return print("소득세는", int(tax/10000), "만원")


calculate_tax(45000000)


# 1부터 10까지의 구구단. 순서는 큰 수부터
for i in range(1, 10):
    for j in range(9, 0, -1):
        print(i * j, end=' ')
    print()


# 별(*)표시를 하향으로 반 피라미드 형태의 패턴 출력
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()


# Quiz3
import shutil
#shutil.copy("test1.txt", "test2.txt")
#shutil.copy2("test1.txt", "test2.txt")
# with open("test1.txt", "rb") as fsrc, open("test2.txt", "wb") as fdst:
#     shutil.copyfileobj(fsrc, fdst)
shutil.copyfile("test1.txt", "test2.txt")

fp = open("test1.py", "a+")
print(fp.tell())
fp.seek(10)
print(fp.read())
str_list = ["print", "(", "\"hello\"", ")", "\n"]
fp.writelines(str_list)

new_file = open("delete_test.txt", "x+")
new_file.write("test!")
new_file.seek(0)
print(new_file.read())
new_file.close()


import os
# os.remove('delete_test.txt')
os.unlink('delete_test.txt')
print(os.listdir())
