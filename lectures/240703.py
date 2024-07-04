coffee_menu = "에스프레소, 아메리카노, 카페라떼, 바닐라라떼"
print(coffee_menu)
print(coffee_menu.split(","))

coffee_menu = ["에스프레소", "아메리카노", "카페라떼", "바닐라라떼"]
print(','.join(coffee_menu))

coffee_menu = " 아바라 "
print(coffee_menu)
print(coffee_menu.strip())

coffee_menu = "에스프레소스"
print(coffee_menu.strip("스"))

coffee_menu = "111아바라111"
print(coffee_menu.lstrip("1"))
print(coffee_menu.rstrip("1"))


def log(s):
    global text
    text += s
    return text


text = ''
print(log('I am'))
print(log(' hungry'))


# input() 입력한 값 중에 첫번째, 중간, 마지막 문자만 출력하시오. 홀수면 중간 문자 짝수면 왼쪽 문자.
string = input()
print(''.join([string[0], string[(len(string)-1)//2], string[-1]]))


# input() 입력한 문자열에서 대문자만 출력하시오.
string = input()
print(''.join(list(filter(lambda c: c.isupper(), string))))


# 두개의 문자열에서 문자를 각각 하나씩 순서대로 조합하여 출력해보세요
s1, s2 = "box", "samples"
s3 = ""
if len(s1) <= len(s2):
    short_string = s1
    long_string = s2
else:
    short_string = s2
    long_string = s1

for i in range(len(short_string)):
    s3 += s1[i] + s2[i]

s3 += long_string[len(short_string):]
print(s3)

# zip: iterable 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 반환
for c1, c2 in zip(s1, s2):
    print(c1, c2)


# 입력한 값에서 대문자는 소문자로 소문자는 대문자로 출력하시오.
string = input()
print(''.join(list(map(lambda c: c.lower() if c.isupper() else c.upper(), string))))

#####
print(string.swapcase())


# 제시된 값에서 짝수와 홀수로 나누어 출력하시오.
list1 = [3, 6, 9, 11, 15, 18, 21]
list2 = [4, 8, 12, 16, 22, 24, 32]
even_list = []
odd_list = []

for num in list1 + list2:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("짝수", even_list)
print("홀수", odd_list)


# 제시된 리스트에서 작은 수에서 큰 수대로 재배열하시오.
def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    pivot = num_list[len(num_list) // 2]
    left, equal, right = [], [], []
    for num in num_list:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort(left) + equal + quick_sort(right)


list1 = [54, 44, 27, 79, 1, 51, 3, 6, 41]
print(quick_sort(list1))
#####
print(sorted(list1))


# 제시된 리스트에서 중복을 제거한 다음 큰 수에서 작은 수로 재배열해주세요.
list1 = [54, 5, 6, 44, 27, 79, 1, 54, 3, 6, 44, 41, 54, 79, 8, 30, 99]
list1 = set(list1)
print(list(reversed(sorted(list1))))
#####
print(sorted(list1, reverse=True))


# 제시된 리스트에서 각각의 숫자가 몇 자릿수인지 dictionary 방식으로 출력하시오.
def calculate_digit(number):
    digit = 0
    while number > 0:
        number //= 10
        digit += 1
    return digit


list1 = [54, 5, 6, 44, 27, 79, 1, 54, 3, 6, 44, 41, 54, 79, 8, 30, 99]
dict1 = {}
for num in list1:
    dict1[str(num)] = str(calculate_digit(num))

print(dict1)


# 제시된 값을 set 로 묶어서 표현하는 코드를 작성하시오.
list1 = [3, 6, 9, 11, 15, 18, 21]
list2 = [4, 8, 12, 16, 22, 24, 32]
set1 = set()
for i in range(len(list1)):
    tup = (list1[i], list2[i])
    set1.add(tup)

print(set1)
#####
set1 = set((x, y) for x, y in zip(list1, list2))
print(set1)


# 제시된 두 개의 set 에서 중복된 값을 찾고 첫번째 집합에서 해당 중복 값을 제거하여 출력하시오.
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
duplicate = set1.intersection(set2)
set1.difference_update(set2)
print(f"중복값: {duplicate}, 제거된 집합: {set1}")


# dict에 값이 numbers에 존재하면 존재하는 숫자값들을 출력하시오.
numbers = [47, 64, 69, 37, 76, 83, 95, 97]
dictionary = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 90}
exist = [value for value in dictionary.values() if value in numbers]
print(exist)


# 키와 값으로 이루어진 dictionary 의 값을 출력하되 중복되지 않게 출력하시오.
dictionary = {'Jan': 47, 'Feb': 52, 'March': 47, 'April': 44, 'May': 52, 'June': 53, 'July': 54, 'Aug': 44, 'Sep': 54}
print(list(set(dictionary.values())))


# 모듈화
import os

print(os.getcwd())
print(os.getlogin())
print(os.getpid())


# 디렉토리 삭제
def delete_dir(dir_path):
    if os.path.exists(dir_path):
        for file in os.scandir(dir_path):
            os.remove(file.path)  # 휴지통에도 안 감
            print(f"file<{file.path}> removed")
        os.rmdir(dir_path)
        return 'Remove All File&Directory'
    else:
        return dir_path + ' Directory Not Found'


os.makedirs('test')
with open('test/test.txt', 'w') as f:
    pass

print(delete_dir('test'))


#import googlemaps as gm
import mymodule as md

md.test()
MyUtil = md.ChildMyUtil(100)  # 클래스 생성
MyUtil.Test()  # 클래스 내 함수 호출
print(MyUtil.val1)  # 부모 클래스의 변수를 자식 클래스가 사용 -> 상속
# print(MyUtil.__val2)  # protected variable


# 두 개의 리스트를 결합하여 다음과 같은 결과를 출력하시오.
# ['My', 'name', 'is', 'Python']
list1 = ['M', 'na', 'i', 'Py']
list2 = ['y', 'me', 's', 'thon']
comb_list = []
for i in range(len(list1)):
    comb_list.append(list1[i] + list2[i])
print(comb_list)
### zip
comb_list = []
for x, y in zip(list1, list2):
    comb_list.append(x + y)
print(comb_list)


# 두 개의 리스트를 결합하여 다음과 같은 결과를 출력하시오.
# 10 400
# 20 300
# 30 200
# 40 100
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(list1[i], list2.pop())


# 키와 값을 결합하여 dictionary 타입으로 출력하시오. zip 활용
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
comb_dict = dict(zip(keys, values))
print(comb_dict)


# 해당 dictionary 에서 history 의 값을 출력하시오.
sample_dict = {
    "class": {
        "name": "Mike",
        "marks": {
            "physics": 70,
            "history": 80
        }
    }
}
print("history:", sample_dict["class"]["marks"]["history"])


# sample_dict 의 모든 값을 비교하여 name 과 salary 키의 값만 출력하시오.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
new_dict = dict()
new_dict[keys[0]] = sample_dict[keys[0]]
new_dict[keys[1]] = sample_dict[keys[1]]
print(new_dict)


# sample_dict에서 최소 및 최대값을 출력하시오.
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'History': 75,
}
print(max([score for score in sample_dict.values()]))


# Quiz1
# 1) 해당 리스트에서 데이터가 없는 경우를 제외하고 출력하도록 해보세요.
# 데이터 없는 경우를 제외하기 위해서 반드시 filter() 를 활용해서 해결해보세요
list1 = ["Mike", "", "Emma", "Kelly", "Brad"]
print(list(filter(lambda name: name != "", list1)))


# 2) 6000 다음에 7000 값을 추가하는 코드를 짜보세요
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


# 3)  symmetric_difference와 symmetric_difference_update 의 차이를 이해할 수 있는 코드를 구현하고
# 주석으로 부가적인 설명을 반영해주세요
set_A = {2, 4, 6, 8, 10, 12}
set_B = {3, 6, 9, 12, 15}
print(set_A.symmetric_difference(set_B))  # symmetric_difference: 집합 A와 집합 B의 대칭 차집합을 반환
set_A.symmetric_difference_update(set_B)  # symmetric_difference_update: 집합 A를 집합 A와 집합 B의 대칭 차집합으로 변경
print(set_A)


# 4) intersection과 intersection_update 의 차이를 이해할 수 있는 코드를 구현하고
# 주석으로 부가적인 설명을 반영해주세요
set_A = {2, 4, 6, 8, 10, 12}
set_B = {3, 6, 9, 12, 15}
print(set_A.intersection(set_B))  # intersection: 집합 A와 집합 B의 교집합을 반환
set_A.intersection_update(set_B)  # intersection_update: 집합 A를 집합 A와 집합 B의 교집합으로 변경
print(set_A)


# 5) tuple1 = (10, 20, 30, 40, 50) 를 Reverse 하는 코드를 짜보세요
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple(reversed(tuple1))
print(tuple1)


# 6) tuple1 에서 20 이란 값을 추출하는 코드를 짜보세요
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


# 7) sampleDict 의 모든 값을 비교하여 name과 salary 키를 제거하고 출력하는 코드를 작성해보세요
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
sample_dict.pop("name")
sample_dict.pop("salary")
# del sample_dict["name"]
# del sample_dict["salary"]
print(sample_dict)


# 8) sample_dict 에서 name의 Brad 에 있는 salary 값을 변경하여 출력해보세요
sample_dict = {
    'emp1': {'name': 'Brad', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500},
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
