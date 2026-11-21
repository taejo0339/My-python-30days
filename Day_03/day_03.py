# Arithmetic Operations in Python
# 파이썬의 산술 연산

# # <산술 연산자>
# print('Addition: ', 1 + 2)
# print('더하기: ', 1 + 2)
# print('Subtraction: ', 2 - 1)
# print('빼기: ', 2 - 1)
# print('Multiplication: ', 2 * 3)
# print('곱하기: ', 2 * 3)
# # Division in python gives floating number
# # 파이썬에서 나눗셈은 실수(소수)를 결과로 준다.
# print('Division: ', 4 / 2) # 2.0
# print('Division: ', 6 / 2) # 3.0
# print('나눗셈: ', 7 / 2)   # 3.5
# # gives without the floating number or without the remaining
# # 소수점 없이, 또는 나머지 없이 (결과를)준다.
# print('Division without the ramainder: ', 7 // 2)
# print('나머지 없는 나눗셈(몫): ', 7 // 2)
# print('Modulus: ', 3 % 2)               # Gives the remainder 나머지를 준다
# print('나머지 없는 나눗셈(몫): ', 7 // 3)
# print('Exponential: ', 3 ** 2)          # it means 3 * 3 (3 * 3이라는 뜻)
# print('거듭제곱: ', 3 ** 2)

# # Floating numbers
# # 실수
# print('Floating Number,PI', 3.14)
# print('실수, 원주율(PI)', 3.14)
# print('Floating Number, gravity', 9.81)

# # Complex numbers
# # 복소수
# print('복소수: ', 1+1j)
# print('복소수 곱하기: ', (1+1j) * (1-1j))

# # Declaring the variable at the top first
# # 맨 위에서 변수를 먼저 선언하기

# # a is a variable name and 3 is an integer data type
# # a는 변수 이름이고, 3은 정수 자료형이다.
# a = 3  

# # b is a variable name and 3 is an integer data type
# # b는 변수 이름이고, 2는 정수 자료형이다.
# b = 2

# # Arithmetic operations and assigning the result to a variable
# # 산술 연산을 하고 그 결과를 변수에 저장하기
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
# # total 대신 sum이라는 이름을 쓰고 싶었지만, sum은 내장 함수라서
# # 내장 함수 이름을 덮어쓰지 않도록 피하는 게 좋다
# print(total) # if you don't label your print with some string, you never know from where is  the result is coming
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# # Declaring values and organizing them together
# # 값을 선언하고 함께 정리하기
# num_one = 3
# num_two = 4

# # Arithmetic operations
# # 산술 연산
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_two
# remainder = num_two % num_one

# # Printing values with label
# # 설명 글자를 붙여서 출력하기
# print('total: ', total)         # total = 합계  
# print('difference: ', diff)     # difference = 차이
# print('product: ', product)     # product = 곱
# print('division: ', div)        # division = 나눗셈
# print('remainder: ', remainder) # remainder = 나머지

# # Calculating area of a circle
# # 원의 넓이 계산하기
# radius = 10                             # 원의 반지름
# # two * sign means exponent or power
# # 별표 두 개(**)는 지수, 즉 거듭제곱을 뜻한다
# area_of_circle = 3.14 * radius ** 2     # 두 개의 * 기호는 지수를 의미합니다
# print('Area of a circle: ',area_of_circle)

# # Calculating area of a rectangle
# # 직사각형의 넓이 계산하기
# length = 10
# width = 20
# area_of_circle = length * width
# print('Area of rectangle: ', area_of_circle) # 직사각형의 넓이 출력

# # Calculating a weight of an object
# # 물체의 무게 계산하기
# mass = 75               # 질량
# gravity = 9.81          # 중력 가속도
# weight = mass * gravity # 무게
# print(weight, 'N')      # N = 뉴턴 (힘의 단위)

# # <비교 연산자>
# # True, because 3 is greater than 2
# # True, 3이 2보다 크니까 
# print(3 > 2)

# # True, because 3 is greater than 2
# # True, 3이 2보다 크니까 
# print(3 >= 2) 

# # False,  because 3 is greater than 2
# # False, 3이 2보다 크니까
# print(3 < 2)

# # True, because 2 is less than 3
# # True, 2가 3보다 작으니까
# print(2 < 3)

# # True, because 2 is less than 3
# # True, 2가 3보다 작으니까
# print(2 <= 3)

# # False, because 3 is not equal to 2
# # False, 3과 2는 같지 않으니까
# print(3 == 2)

# # True, because 3 is not equal to 2
# # True, 3과 2는 같지 않으니까
# print(3 != 2)
# print(len('mango') == len('avocado'))   # False
# print(len('mango') != len('avocado'))   # True
# print(len('mango') < len('avocado'))    # True
# print(len('milk') != len('meat'))       # False
# print(len('milk') == len('meat'))       # True
# print(len('tomato') == len('potato'))   # True
# print(len('python') > len('dragon'))    # False

# # Boolean comparison
# # 불리언 비교
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False: ', False == False)
# print('True and True: ', True and True)
# print('True or False: ', True or False)

# # Another way comparison
# # 또 다른 비교 방법
# # True - because the data values are the same
# # True - 데이터 값이 같으니까
# # _is_: 두 변수가 동일할 경우 참을 반환합니다.(x is y)
# # _is not_: 두 변수가 동일하지 않을 경우 참을 반환합니다.(x is not y)
# # _in_: 제시된 목록에 특정 항목이 포함된 경우 참을 반환합니다.(x in y)
# # _not in_: 제시된 목록에 특정 항목이 없으면 참을 반환합니다.(x in y)
# print('1 is 1', 1 is 1)
# print('1 is not 2', 1 is not 2)         # True - because 1 is not 2 (1은 2가 아니니까)
# print('A in Ataejo', 'A' in 'Ataejo')     # True - A found in the string (문자열 안에 A가 있다)
# print('B in taejo', 'B' in 'taejo')       # False - there is no uppercase B (대문자 B가 없다)
# # True - because coding for all has the word coding
# # True - 'coding for all' 안에 'coding'이라는 단어가 있으니까
# print('coding' in 'coding for all')
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 **2)   # True

# # <논리 연산자>
# # True - because both statements are true
# # True - 두 조건이 모두 참이니까
# print(3 > 2 and 4 > 3)  

# # False - because the second statement is false
# # False - 두 번째 조건이 거짓이니까
# print(3 > 2 and 4 < 3)

# # False - because both statements are false
# # False - 두 조건이 모두 거짓이니까
# print(3 < 2 and 4 < 3)

# # True - because both statements are true
# # True - 두 조건이 모두 참이니까
# print(3 > 2 or 4 > 3)

# # True - because both statements are true
# # True - 조건 중 하나가 참이니까
# print(3 > 2 or 4 < 3)

# # False - because both statements are false
# # False - 두 조건이 모두 거짓이니까
# print(3 < 2 or 4 < 3)

# # False - because 3 > 2 is true, then not True gives False
# # False - 3 > 2는 True인데, not True는 False가 된다
# print(not 3 > 2)

# # False - Negation, the not operator turns true to false
# # False - 부정: not 연산자는 참을 거짓으로 바꾼다
# print(not True)

# print(not False)     # True
# print(not not True)  # True
# print(not not False)  # False

# Exercises - Day 3
# age = 20
# height = 160.0
# complex_num = 4 + 4j

# input()은 사용자가 무엇을 입력하든 항상 문자열(str)로 돌려줘요. 숫자를 입력해도요.
# input() = 항상 문자열 계산에 쓰려면 int()나 float()로 꼭 바꿔야 해요!
# HALF = 0.5
# base = int(input('Enter base: '))
# height = int(input('Enter height: '))
# area_of_triangle = HALF * base * height
# print('The area of the triangle is', area_of_triangle)

# side_a = int(input('Enter side a: '))
# side_b = int(input('Enter side b: '))
# side_c = int(input('Enter side c: '))
# print('The perimeter of the triangle is', side_a + side_b + side_c)

# 직사각형 = rectangle, 정사각형 = square, 원 = circle, 삼각형 = triangle
# length = float(input('길이: '))
# width = float(input('폭: '))
# rectangle = length * width
# print('면적 : ', rectangle)
# print('둘레 : ', 2 * (length + width))

# radius = float(input('반지름: '))
# area_of_circle = 3.14 * radius ** 2
# print('원의 면적: ', area_of_circle)

# circumference = 2 * 3.14 * radius
# print('원의 둘레: ', circumference)

# y = 2x - 2의 기울기
# x 절편, y 절편 구하시오
# <중학교 수학 개념>
# 기울기: y = mx + b 모양에서 m은?
# y절편: x 자리에 0을 넣으면 y는?
# x절편: y 자리에 0을 넣고 x에 대해 정리하면?

# y = 2x - 2 -> y = mx + b
# m = 2   # 기울기 (x 앞의 숫자)
# b = -2  # y절편 (y 맨 뒤의 숫자)

# slope = m # ("m에 있는 값을 slope에도 넣어 둬" 그래서 나중에 m이 바뀌어도 slope에는 예전 값이 남아 있어요.)
# y_intercept = m * 0 + b  # y절편은 x=0일 때 y를 구하면 됨
# x_intercept = -b / m  # x절편은 y=0일 때 x를 구하면 됨

# print('기울기: ', slope)
# print('y절편: ', y_intercept)
# print('x절편: ', x_intercept)


# # 점(2,2)과 점(6,10) 사이의 거리와 기울기 구하기
# x1, y1 = 2, 2
# x2, y2 = 6, 10
# x_diff = x1 - x2
# y_diff = y1 - y2
# distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
# print('두 점 사이의 거리: ', distance)
# m = (y2 - y1) / (x2 - x1)
# print('두 점 사이의 기울기: ', m)

# print('과제 8과 9의 기울기 비교: ', slope >= m)

# x = int(input('x값을 입력하세요: '))
# y = x**2 + 6*x + 9
# print('x = ', x, '일 때 y = ', y)
# x절편: 그래프가 x축과 만나는 곳 → 이때 y = 0
# y절편: 그래프가 y축과 만나는 곳 → 이때 x = 0

# print(len('python') > len('dragon'))               # False
# print(('on' in 'python') and ('on' in 'dragon'))   # True

# print('jargon' in 'I hope this course is not full of jargon')   # True
#        # 찾는 것        # 찾을 곳

# print(('on' not in 'dragon') and ('on' not in 'python'))        # False

# text = float(len('python'))  # len() = 문자열 길이 구하기
# print(str(text))

# even_num = int(input('숫자를 입력하세요: '))
# print('짝수인가요? ', even_num % 2 == 0)  # 짝수이면 True, 홀수이면 False

# floor_division = 7 // 3
# int_converted_value = int(2.7)
# print(floor_division == int_converted_value)  # True

# print(type('10') == type(10))  # False

# print(int('9.8')) == 10  
# ValueError: invalid literal for int() with base 10: '9.8'
# print(int(float('9.8')) == 10)  # False

# hours = int(input('Enter hours: '))
# rate_per_hour = int(input('Enter rate per hour: '))
# earnings = hours * rate_per_hour
# print('Your weekly earnings is', earnings)

# number_of_years_you_have_lived = int(input('Enter number of years you have lived: '))
# number_of_seconds_you_have_lived = number_of_years_you_have_lived * 365 * 24 * 60 * 60
# print('You have lived for', number_of_seconds_you_have_lived, 'seconds.')

n = 1
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n = 2
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n = 3
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n = 4
print(n, n ** 0, n ** 1, n ** 2, n ** 3)
n = 5
print(n, n ** 0, n ** 1, n ** 2, n ** 3)