# Variables in Python
# 변수 선언
# first_name = 'Jung'
# last_name = 'taejo'
# country = 'South korea'
# city = 'Seoul'
# age = 20
# is_married = False
# skills = ['Python', 'Github', 'AWS']
# person_info = {
#     'firstname' : 'Jung',
#     'lastname'  : 'taejo',
#     'country'   : 'South korea',
#     'city'      : 'Seoul'
# }

# Printing the values stored in the variables
# 변수에 저장된 값들을 출력하기

# print('First name: ', first_name)
# print('First name length: ', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# Declaring multiple variables in one line
# 한 줄에 여러 개의 변수 만들기

# first_name, last_name, country, age, is_married = 'Jung', 'taejo', 'South korea', 20, False

# print(first_name, last_name, country, age, is_married)
# print('First name: ', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# Exercises - Day 2

# # Level 1
# # 1-1.
# # Day_02 폴더 안에 variables.py 파일을 만들었음.
# # 1-2.
# # 'Day 2: 30 Days of python programming'
# # 1-3.
# first_name = 'Jung'
# # 1-4.
# last_name = 'taejo'
# # 1-5.
# full_name = 'Jung taejo'
# # 1-6.
# country = 'South korea'
# # 1-7.
# city = 'Seoul'
# # 1-8.
# age = 20
# # 1-9.
# year = 2026
# # 1-10.
# is_married = False
# # 1-11.
# is_true = True
# 1-12.
# is_로 시작하는 변수는 "~인가요?"라는 질문.
# 질문에 대한 답은 두 가지이다.
# True or False 
# is_light_on = True  
# 1-13.
# -- 클로드 풀이 --
# 클로드 : "파이썬에서는 잘 쓰지 않는 방법이에요"
# 아래의 변수 선언이 파이썬다운 방법이다.
# a, b, c = 1, 2, 3  
# is_married = False ; is_true = True ; is_light_on = False

# Level 2
# 2-1.
# print(type(first_name))
# print(type(last_name))
# print(type(full_name))
# print(type(country))
# print(type(city))
# print(type(age))
# print(type(year))
# print(type(is_married))
# print(type(is_true))
# print(type(is_light_on))
# print(type(a))
# print(type(b))
# print(type(c))
# print(len(first_name))
# print(bool(len(first_name) >= len(last_name)))
# num_1 = 5
# num_2 = 4
# total = num_1 + num_2
# diff = num_1 - num_2
# product = num_1 * num_2
# division = num_1 / num_2
# remainder = num_2 % num_1
# exp = num_1 ** num_2
# floor_division = num_1 // num_2

# 2-1.
# 용어 -> 반경 : 반지름 (radius)
# 원의 둘레 구하는 공식 : 2 * 3.14 * r
# 원의 넓이를 구하는 공식 : 3.14 * r * r
# pi = 3.14
# _area_of_circle_half = 30
# _area_of_circle = pi * (_area_of_circle_half ** 2)
# _circum_of_circum = 2 * pi * _area_of_circle_half
# radius = float(input('반지름을 입력하세요 : '))
# print((radius ** 2) * pi)

# 2-1.
# first_name = input ('성 : ')
# last_name = input('이름 : ')
# country = input('국가 : ')
# age = input('나이 : ')
# 2-2.
# >>> help('keywords')

# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not
