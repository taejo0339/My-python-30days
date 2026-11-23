# # Single line comment
# # 한 줄 주석
# letter = 'P'                # A string could be a single character or a bunch of texts 문자열은 단일 문자 또는 여러 텍스트일 수 있습니다.
# print(letter)               # P
# print(len(letter))          # 1
# greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!" 문자열은 단일 또는 이중 따옴표일 수 있습니다.
# print(greeting)             # Hello, World!
# print(len(greeting))        # 13
# sentence = "I hope you are enjoying 30 days of python challenge"
# print(sentence)

# # Multiline String 여러 줄 문자열
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)
# # Another way of doing the same thing 동일한 작업을 수행하는 또 다른 방법
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# # String Concatenation 문자열 연결
# first_name = 'taejo'
# last_name = 'Jung'
# space = ' '
# full_name = first_name + space + last_name
# print(full_name) # taejo Jung
# # Checking length of a string using len() builtin function 내장 함수 len()을 사용하여 문자열 길이 확인
# print(len(first_name))  # 5
# print(len(last_name))   # 4
# print(len(first_name) > len(last_name)) # True
# print(len(full_name))  # 10

# # Unpacking characters 문자 풀기
# language = 'Python'
# a, b, c, d, e, f = language # unpacking sequence characters into variables 변수에 시퀀스 문자를 풀기
# print(a)    # P
# print(b)    # y
# print(c)    # t
# print(d)    # h
# print(e)    # o
# print(f)    # n

# # Accessing characters in strings by index 인덱스로 문자열의 문자에 액세스
# language = 'Python'
# first_letter = language[0]
# print(first_letter) # P
# second_letter = language[1]
# print(second_letter) # y
# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter)  # n

# # If we want to start from right end we can use negative indexing. -1 is the last index 오른쪽 끝에서 시작하려면 음수 인덱싱을 사용할 수 있습니다. -1은 마지막 인덱스입니다.
# language = 'Python'
# last_letter = language[-1]
# print(last_letter)  # n
# second_last = language[-2]
# print(second_last)  # o

# # Slicing 슬라이싱

# language = 'Python'
# # starts at zero index and up to 3 but not include 3 0번째 인덱스에서 시작하여 3까지 포함하지 않음
# first_three = language[0:3]
# last_three = language[3:6]
# print(last_three)   # hon
# # Another way 또 다른 방법
# last_three = language[-3:]
# print(last_three)   # hon
# last_three = language[3:]
# print(last_three)   # hon

# # Skipping character while splitting Python strings Python 문자열을 분할하는 동안 문자 건너뛰기
# language = 'Python'
# pto = language[0:6:2]
# print(pto)  # pto

# # Escape sequence 이스케이프 시퀀스
# print('I hope everyone is enjoying the Python Challenge.\nDo you ?') # \n means new line
# print('Days\tTopics\tExercises')
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
# print('THis is a back slash symbol (\\)') # \ means backslash 
# print('In every programming language it starts with \"Hello, World!\"') # \" means double quote

# # String Methods 문자열 메서드
# # capitalize() : Converts the first character of the string to uppercase and the rest to lowercase. 문자열의 첫 번째 문자를 대문자로, 나머지를 소문자로 변환합니다.

# challenge = 'thirty days of python'
# print(challenge.capitalize()) # 'Thirty days of python'

# # count() : returns occurences of substring in string, count(substring, start=.., end=..) 문자열의 하위 문자열 발생 횟수를 반환합니다. count(substring, start=.., end=..)

# challenge = 'thirty days of python'
# print(challenge.count('y')) # 3
# print(challenge.count('y', 7, 14)) # 1
# print(challenge.count('th')) # 2

# # endswidth() : Checks if a string ends with a specified ending, returns True or False. 문자열이 지정된 끝으로 끝나는지 확인하고 True 또는 False를 반환합니다.

# challenge = 'thirty days of python'
# print(challenge.endswith('on')) # True
# print(challenge.endswith('tion')) # False

# # expandtabs() : Replace tab character with spaces, default tab size is 8. 탭 문자를 공백으로 바꾸고 기본 탭 크기는 8입니다.

# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs()) # 'thirty  days    of      python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# # find() : Returns the index of first occurrence of substring 문자열의 첫 번째 하위 문자열 발생 인덱스를 반환합니다.

# challenge = 'thirty days of python'
# print(challenge.find('y')) # 6
# print(challenge.find('th')) # 0

# # format() : formats the string into a nicer output 문자열을 더 깔끔한 출력으로 형식화합니다.
# first_name = 'taejo'
# last_name = 'Jung'
# job = 'student'
# country = 'Korea'
# sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
#     first_name, last_name, job, country)
# print(sentence) # I am taejo Jung. I am a student. I live in Korea.

# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal 소수점 아래를 두 자리로 제한한다
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a % b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# '''
# # output
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64
# '''

# # strings and numbers
# radius = 10
# pi = 3.14
# area = pi # radius ## 2
# result = 'The area of circle with {} is {:.2f}'.format(str(radius), str(area)) # 2 digits after decimal
# print(result)   # The area of circle with 10 is 314.0

# # index() : Returns the index of substring 부분 문자열의 인덱스(위치 번호)를 돌려준다
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isalnum(): Checks alphanumeric character 알파벳이나 숫자로만 이루어졌는지 확인

# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum())  # True

# challenge = '30DaysPython'
# print(challenge.isalnum())  # True

# challenge = 'thirty days of python'
# print(challenge.isalnum())  # False

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum())  # False

# # isalpha(): Checks if all characters are alphabets 모든 글자가 알파벳인지 확인

# challenge = 'thirty days of python'
# print(challenge.isalpha())  # True
# num = '123'
# print(num.isalpha())    # False

# # isdecimal(): Checks Decimal Characters 10진수 숫자로만 이루어졌는지 확인

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isdigit(): Checks Digit Characters 숫자 글자로만 이루어졌는지 확인

# challenge = 'Thirty'
# print(challenge.isdigit())  # False
# challenge = '30'
# print(challenge.isdigit())  # True

# # isdecimal(): Checks decimal characters 10진수 숫자로만 이루어졌는지 확인

# num = '10'
# print(num.isdecimal())  # True
# num = '10.5'
# print(num.isdecimal())  # False

# # isidentifier(): Checks for valid identifier means it check if a string is a valid variable name 올바른 식별자인지 확인, 즉 변수 이름으로 쓸 수 있는 문자열인지 확인

# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number False, 숫자로 시작하니까
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

# # islower(): Checks if all alphabets in a string are lowercase 문자열의 모든 알파벳이 소문자인지 확인

# challenge = 'thirty days of python'
# print(challenge.islower())  # True
# challenge = 'Thirty days of python'
# print(challenge.islower())  # False

# # isupper(): returns if all characters are uppercase characters 모든 글자가 대문자인지 알려 줌

# challenge = 'thirty days of python'
# print(challenge.isupper())  # False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper())  # True

# # isnumeric(): Checks numeric characters 숫자를 나타내는 글자로만 이루어졌는지 

# num = '10'
# print(num.isnumeric())      # True
# print('ten'.isnumeric())    # False

# # join(): Returns a concatenated string 이어 붙인 문자열을 돌려줌

# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '#, '.join(web_tech)
# print(result)   # 'HTML# CSS# JavaScript# React'

# # strip(): Removes both leading and trailing characters 앞쪽과 뒤쪽 끝의 글자를 제거

# challenge = 'thirty days of python'
# print(challenge.strip('y')) # 5

# # replace(): Replaces  substring inside 안에 있는 부분 문자열을 다른 것으로 바꿈

# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding'))

# # split(): Splits String from Left 문자열을 왼쪽부터 쪼갬

# challenge = 'thirty days of python'
# print(challenge.split())    # ['thirty', 'days', 'of', 'python']

# # title(): Returns a Title Cased String 각 단어의 첫 글자를 대문자로 바꾼 문자열을 돌려줌

# challenge = 'thirty days of python'
# print(challenge.title())  # Thirty Days Of Python

# # swapcase(): Swaps uppercase to lowercase and lowercase to uppercase 대문자는 소문자로, 소문자는 대문자로 서로 바꾼다

# challenge = 'thirty days of python'
# print(challenge.swapcase()) # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days of Python'
# print(challenge.swapcase()) # # tHIRTY dAYS oF pYTHON

# # startswith(): Checks if String Starts with the Specified String 문자열이 지정한 문자열로 시작하는지 확인

# challenge = 'thirty days of python'
# print(challenge.startswith('thirty'))  # True
# challenge = '30 days of python'
# print(challenge.startswith('thirty'))  # False

# Exercises - Day 4
# 1. 문자열 'Thirty', 'Days', 'Of', 'Python'을
#    단일 문자열 'Thirty Days Of Python'에 연결합니다.
# a = 'Thirty'
# b = 'Days'
# c = 'Of'
# d = 'Python'
# space = ' '
# full_str = a + space + b + space + c + space + d
# print(full_str)

# 2. 문자열 'Coding', 'For' , 'All'을
#    단일 문자열 'Coding For All'에 연결합니다.
# c = 'Coding'
# f = 'For'
# a = 'All'
# space = ' '
# connect = c + space + f + space + a
# print(connect)

# 3. company라는 변수를 선언하고
#    초기 값 "Coding For All"에 할당합니다.
# 클로드 해석 : "company 변수를 만들어서 'Coding For All'이라는 문자열을 넣으세요."
company = "Coding For All"

# 4. *print()* 를 사용하여 회사 변수를 인쇄합니다.
# print(company)

# 5. *len()* 메서드와 *print()* 를 사용하여
#    회사 문자열의 길이를 인쇄합니다.
# print(len(company))

# 6. *upper()* 메서드를 사용하여 모든 문자를 대문자로 변경합니다.
# print(company.upper())

# 7. *lower()* 메서드를 사용하여 모든 문자를 소문자로 변경합니다.
# print(company.lower())

# 8. 문자열 *Coding For All* 의 값을 형식화하려면
#    capitalize(), title(), swapcase() 메소드를 사용하십시오.
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# 9. *Coding For All* 문자열의 첫 번째 단어를 잘라냅니다.
print(company[0:6])

# 10. Index, find 또는 기타 방법을 사용하여 
# *Coding For All* 문자열에 단어 Coding이 포함되어 있는지 확인합니다.
# include_str = 'Coding'
# print(company.index(include_str))
# print(company.find(include_str))

# 11. 문자열 'Coding For All'의 Coding이라는 단어를 Python으로 바꿉니다.
# print(company.replace('Coding','Python'))

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
# all = "Python for Everyone"
# print(all.replace('Everyone', 'All'))

# 13. 공백을 구분 기호로 사용하여 문자열 'Coding For All'을 분할합니다(split()).
# coding = 'Coding For All'
# print(coding.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"은 쉼표에서 문자열을 나눕니다.
# it_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# print(it_company.split(','))

# 15. 문자열 *Coding For All* 에서 인덱스 0에 있는 문자는 무엇입니까?
test = 'Coding For All'
# print(test[0])

# 16. What is the last index of the string Coding For All. 문자열 Coding For All의 마지막 인덱스는 몇 번인가요?
print(test.rfind('l'))

# 17. "Coding For All" 문자열에서 인덱스 10에 있는 문자는 무엇입니까?
# print(test[10])

# 18. 'Python For Everyone'이라는 이름의 약어 또는 약어를 만듭니다.
# 약어(acronym) = 각 단어의 첫 글자만 모아서 만든 줄임말이에요.
# acronym = 'Python For Everyone'
# print(acronym[0] + acronym [7] + acronym[11]) # 글자 하나를 꺼낼 때마다 변수[번호] 모양을 따로따로 써야 해요. 그리고 꺼낸 글자들 사이에 +를 넣으면 돼요

# 19. 'Coding For All'이라는 이름의 약어 또는 약어를 만듭니다.
# print(test[0] + test[7] + test[11])

# 20. Index를 사용하여 Coding For All에서 C가 처음 나타나는 위치를 결정합니다.
# print(test.index('C'))

# 21. Index를 사용하여 Coding For All에서 F가 처음 나타나는 위치를 결정합니다.
# print(test.index('F'))

# 22. Coding For All People에서 l(소문자 l)이 마지막으로 나타나는 위치를 결정하려면 rfind를 사용하십시오.
# test_add = 'Coding For All People'
# print(test_add.rfind('l'))

# 23. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 처음 'because'가 처음 나오는 위치는?
challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge.find('because'))

# 24. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 'because'가 마지막에 나오는 위치는?
print(challenge.rfind('because'))

# 25. 색인 또는 찾기를 사용하여 다음 문장에서 'because because because' 구절을 잘라내기 (Slice out)
print(challenge[31:54])

# 26. 색인 또는 찾기를 사용하여 다음 문장에서 'because'가 처음 나오는 위치는?
print(challenge.index('because'))

# 27. 다음 문장에서 'because because because' 구절을 잘라내기 (음수 인덱스로 해보기, 슬라이싱은 항상 왼쪽 -> 오른쪽)
print(challenge[-40:-17])

# 28. 'Coding For All'은 하위 문자열 *Coding* 으로 시작합니까?
a = 'Coding For All'
print(a.startswith('Coding'))

# 29. 'Coding For All'은 하위 문자열 *coding* 으로 끝납니까?
print(a.endswith('coding'))

# 30. ' Coding For All ' , 주어진 문자열에서 왼쪽 및 오른쪽 후행 공백을 제거합니다.
text = ' Coding For All ' # 공백을 지울 때는 괄호를 비운다
print(text.strip())

# 31. 다음 변수 중 isidentifier() 메서드를 사용할 때 True를 반환하는 변수는 무엇입니까?
#    - 30DaysOfPython
#    - thirty_days_of_python
a = '30DaysOfPython' 
print(a.isidentifier())         # False (변수 이름은 숫자로 시작할 수 없다, 알파벳, 숫자, 밑줄만 쓸 수 있다.)
a = 'thirty_days_of_python'
print(a.isidentifier())         # True

# 32. 다음 목록에는 일부 파이썬 라이브러리의 이름이 포함되어 있습니다: 
#  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
#  공백 문자열이 있는 해시로 목록에 가입하십시오.
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(library)
print(result)

"""
33. 새 줄 이스케이프 시퀀스를 사용하여 다음 문장을 구분합니다.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
"""
print("I am enjoying this challenge.\nI just wonder what is next.")

"""
34. 새 줄 이스케이프 시퀀스를 사용하여 다음 문장을 구분합니다.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
"""
print("Name\tAge\tCountry\tCity\ntaejo\t250\tKorea\tSeoul")

"""
35. 문자열 형식 지정 방법을 사용하여 다음을 표시합니다: 

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```
"""
pi = 3.14
radius = 10
area = pi * radius ** 2
formated_string = 'The area of a circle with radius 10 is 314 meters square.'
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')


"""
1. 문자열 형식화 방법을 사용하여 다음을 작성하십시오:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```
"""
# 지금처럼 값을 바로 넣어 출력하는 경우에는 f-string이 가장 좋아요. 
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') # 반드시 {} 안에서, 값 다음에 와야 해요!
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
