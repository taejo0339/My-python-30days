# Day01
# 자료형 - 숫자
# print("Hello world!")

# print(2 + 3)  # 덧셈 연산자 addition(+)
# print(3 - 1)  # 뺄셈 연산자 subtraction(-)
# print(2 * 3)  # 곱셈 연산자 multiplication(*)
# print(3 / 2)  # 나눗셈 연산자 division(/)
# print(3 ** 2) # 제곱 연산자 exponential(**)
# print(3 % 2)  # 나머지 연산자 modulus(%)

# Data types (자료형)
# 숫자형 (Number)
# print(type(10))                  # Int 정수형
# print(type(3.14))                # Float 실수형
# print(type(1 + 3j))              # Complex 복소수형
# print(type('taejo'))             # String 문자열형
# print(type([1, 2, 3]))           # List 리스트형
# print(type({'name' : 'taejo'}))  # Dictionary 딕셔너리
# print(type({99.1, 3.14, 11.19})) # Set 세트형
# print(type((100, 101, 203)))     # Tuple 튜플형

# list[]                : 순서있는 목록, 수정 가능
# Tuple()               : 순서있는 목록, 수정 불가
# Dictionary{key:value} : 이름표로 찾는 저장소
# set{}                 : 순서없는 모음, 중복 불가

# Exercises - Day 1

# Level 1
# 1단계 : 대화형 셸을 열기 -> win+R키 -> cmd 검색 -> python 입력
# C:\Users\taejo>python --version
# Python 3.14.3

# 2단계 : 
# >>> 3 + 4
# 7
# >>> 3 - 4
# -1
# >>> 3 * 4
# 12
# >>> 3 % 4
# 3
# >>> 3 / 4
# 0.75
# >>> 3 ** 4
# 81
# >>> 3 // 4
# 0

# 3단계 :
# >>> type(str('Josephine'))
# <class 'str'>
# --클로드 풀이-- 
# '따옴표'로 감싸는 순간 이미 문자열이라서
#  str()은 필요 없어요.
# 그리고 문제는 "문자열을 써 보라"는 거라서
# 셸에 'Josephine'만 입력해도 돼요.

# >>> type(str('Joice'))
# <class 'str'>
# >>> type(str('Republic of Korea'))
# <class 'str'>
# >>> type(str('I am enjoying 30 days of python'))
# <class 'str'>

# 4단계 :
# >>> type(10)
# <class 'int'>
# >>> type(9.8)
# <class 'float'>
# >>> type(3.14)
# <class 'float'>
# >>> type(4 - 4j)
# <class 'complex'>
# >>> type(['taejo', 'cyber security', 'South Korea'])
# <class 'list'>
# >>> type('Josephine')
# <class 'str'>
# >>> type('Joice')
# <class 'str'>
# >>> type('Republic of Korea')
# <class 'str'>

# Level 2
# print(('1. 사용 중인 Python 버전 확인\n') * 3)
# print(('2. Python 대화형 셸을 열고 다음 작업을 수행합니다. 피연산자는 3과 4입니다.\n') * 3)
# print(('3. Python 대화형 셸에 문자열을 씁니다. 문자열은 다음과 같습니다.\n') * 3)
# print(('4. 다음 데이터의 데이터 유형을 확인하십시오.\n') * 3)
# -- 클로드 풀이 --
# "Level 1에서 셸(>>>)로 했던 걸, 이번엔 .py 파일에 코드로 써서 똑같이 해 보세요."

# *재풀이*
# 2-1. 
# import sys
# print(sys.version)

# 2-2.
# print(3 + 4)
# print(3 - 4)
# print(3 * 4)
# print(3 % 4)
# print(3 / 4)
# print(3 ** 4)
# print(3 // 4)

# 2-3.
# print('Josephine')
# print('Joice')
# print('Republic of Korea')
# print('I am enjoying 30 days of python')
# --클로드 풀이 --
# print('Josephine')                  # ✅ 이걸로 충분
# print(type('Josephine'))            # ✅ 자료형 확인하고 싶을 때
# print(type(str('Josephine')))       # 😅 틀린 건 아니지만 str()은 쓸모없음

# 2-4.
# print(type(10))
# print(type(9.8))
# print(type(3.14))
# print(type(4 - 4j))
# print(type(['Asabeneh', 'Python', 'Finland']))
# print(type('Josephine'))
# print(type('Joice'))
# print(type('Republic of Korea'))

# Level 3
# print(4 + 3)
# print(1.2 + 3.4)
# print(4 + 3j)
# print('안녕' + '하세요')
# print(type(True))
# print(['Hello', 'my friend'])        # list
# print((123, 456, 789))               # Tuple
# print({123, 456, 789})               # Set     
# print({123:"앞 번호", 456:"뒷 번호"}) # Dictionary

# Euclidean distace 유클리드 거리
# (2, 3) 과 (10, 8) 사이
# print((((2 - 10) **2) +  ((3 - 8) **2)) ** 0.5)

