# 자료형 Set
a = {1, 2, 3, 4, 5}  # a는 전역변수
c = [10, 20, 30]  # c는 전역변수


# argument(인자) / element(요소)
# parameter(매개변수)
def test(b):  # b->parameter
    b = 20
    global a  # 전역 변수를 내부에서 정의할 때
    a = {1, 2, 3}  # a는 전역변수. 1->element
    c = [11, 22, 33]  # c는 지역변수


test(10)  # 10->argument
print(a)  # a->element. 내장 함수


# 빈 값([], '', 0)이면 false
print(bool(0), bool(3.14159), bool(-3), bool(1.0 + 1j))

# 복소수(complex) : 실수 + 허수
print(1 + 1j)
print(complex(1, 1))

# string 할당
str1 = '''str1'''
str2 = """str2"""

print(str1, str2)


def test():
    return  # return null


print(bool(test()))

# 내장 함수 https://docs.python.org/3/library/functions.html
'''
sum()
bool()
chr()
dict()
oct()
slice()
pow()
exec()
eval()
bytes()
bin()
ascii()
abs()
set()
list()
tuple()
'''

# 내장 함수 구현 해보기
a = [1, 2, 3, 4, 5]
print(sum(a))


def my_sum(numbers):
    sum_result = 0
    
    # sum_result += numbers[0]
    # sum_result += numbers[1]
    # sum_result += numbers[2]
    
    for num in numbers:
        sum_result += num
    return sum_result


print(my_sum(a))


def multiply(numbers):
    multi_result = 1
    for num in numbers:
        multi_result *= num
    return multi_result


print(multiply(a))


# *매개변수
def multiply(*numbers):
    multi_result = 1
    print(type(numbers), numbers[1])  # tuple
    # numbers[1] = 5  # error
    numbers = list(numbers)  # type cast
    numbers[1] = 5
    print(type(numbers), numbers[1])
    for num in numbers:
        multi_result *= num
    return multi_result


print(multiply(2, 3, 4))


# **매개변수
dic_a = dict(a=1, b=2, c=3)
dic_a2 = {'a': 1, 'b': 2, 'c': 3}  # dic_a == dic_a2

print(dic_a.keys())


def dic(v, **f_dic):
    print(f_dic, type(f_dic), f_dic['a'], v)
    print('f_dic의 키값은', f_dic.keys())

    for key in f_dic.keys():
        print(key, '=', f_dic[key])

    for item in f_dic.items():
        print(item)

    for item_k, item_v in f_dic.items():
        print(item_k, item_v)
    return


dic(10, a=1, b=2, c=3)


# lambda 함수
def f(x, y): return x + y
a = lambda x, y: x + y
a(2, 3)
(lambda x, y: x + y)(2, 3)  # 하나의 함수

print("lambda func : ", (lambda x: x**2)(15))


def func_lambda(**f_dic):
    for item_k, item_v in f_dic.items():
        print(item_k, "lambda result:", (lambda x: x*3)(item_v))


func_lambda(a=1, b=2, c=3)


# 재귀 함수

def recur(x):
    if x == 1:
        return 1
    return x * recur(x-1)


print(recur(5))


# 순회(circuit)하는 객체 : iterator(반복자) cf) 반복문
# [1, 2, 3, 4, 5]
# (1, 2, 3, 4, 5)
# {1, 2, 3, 4, 5}

for element in [1, 2, 3, 4, 5]:  # 반복문
    print(element)
# 내장 함수 iter
a = (1, 2, 3, 4, 5)
it = iter(a)
print(next(it), next(it), next(it))  # next : iterator 다음 불러옴
# iterable vs iterator ?


# None
print(None == True)
print(None == 0)
print(0 == False)

print(bool(None))


def test():
    return


print(bool(test()))


# 인자 전달
def fun1(name, age):
    print(name, age)


fun1(name="Jeon", age=27)
fun1(age=27, name="Jeon")
fun1("Jeon", 27)


# Nested Function(중첩 함수) 가능
def outer_func(a, b):
    def inner_func(c, d):
        return c + d
    return inner_func(a, b)


print(outer_func(5, 10))


# return 순서
def func(a, b):
    return a + b
    return a - b


print(func(5, 10))


# List 참조
a = [10, 20]
b = a
b = b + [30, 40]  # 새로운 리스트 b 생성 후 연산
print(a)
b = a
b += [30, 40]  # 동일한 리스트 객체를 참조하는 a에도 반영
print(a)


# 논리 연산자 AND
x = 100
y = 50
print(x and y)  # x가 True 이면 y, False 이면 x를 반환
