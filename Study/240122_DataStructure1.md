# Data Structure
## 개요
### 데이터 구조 `Data Structure`
여러 데이터를 효과적으로 사용, 관리하기 위한 구조<br>
(str, list, dict 등)
### 자료 구조
- 컴퓨터 공학에서는 ‘자료 구조’ 라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것
    ![image](https://github.com/ragu6963/TIL/assets/32388270/ec3c4025-1305-4ba1-8f7a-fc355c1fa4e3)
### 데이터 구조 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 <span style='color:red;'>메서드</span>를 호출하여 다양한 기능을 활용하기

## 메서드 `Method`
객체에 속한 함수
> 객체의 상태를 조작하거나 동작을 수행

### 메서드 특징
- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 ‘타입을 표현하는 방법’이며 이미 은연중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능

### 메서드 호출 방법
> 데이터 타입 객체.메서드()
```python
'hello'.capitalize()
```

# 시퀀스 데이터 구조
## 문자열
### 문자열 조회/탐색 및 검증 메서드
|        메서드      	|                                         설명                                        	|
|:------------------:	|:-----------------------------------------------------------------------------------:	|
|      s.find(x)     	|     x의   첫 번째 위치를 반환. 없으면,   -1을 반환                                  	|
|      s.index(x)    	|     x의   첫 번째 위치를 반환. 없으면,   오류 발생                                  	|
|     s.isalpha()    	|     알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)    	|
|     s.isupper()    	|     대문자 여부                                                                     	|
|     s.islower()    	|     소문자   여부                                                                   	|
|     s.istitle()    	|     타이틀   형식 여부                                                              	|

#### .find(x)
```python
print('banana'.find('a')) # 1
print('banana'.find('z')) # -1
```

#### .index(x)
```python
print('banana'.index('a')) # 1
# print('banana'.index('z')) # ValueError : substring not found

```

#### .isupper(x) / .islower(x)

```python
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False


str.isupper('HELLO') # 전달인자 있어야함
str.islower('Hello')
string1.isupper('Hello') # 전달인자 있으면 오류


```
- 문자열 전체가 upper/lower 일때만 True
- 일부만 일때는 False
- str.isupper(string) 일때는 전달인자 O
- string1.isupper('Hello') 일때는 전달인자 X

#### .isalpha(x)
```python
string1 = 'HELLO'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False
```

### 문자열 조작 메서드 (새 문자열 반환)
|                  메서드                 	|                                              설명                                            	|
|:---------------------------------------:	|:--------------------------------------------------------------------------------------------:	|
|       s.replace(old,   new[,count])     	|     바꿀 대상 글자를 새로운 글자로 바꿔서 반환                                               	|
|             s.strip([chars])            	|     공백이나 특정 문자를 제거                                                                	|
|     s.split(sep=None,   maxsplit=-1)    	|     공백이나 특정 문자를 기준으로 분리                                                       	|
|       'separator'.join(iterable)      	|     구분자로 iterable을   합침                                                               	|
|              s.capitalize()             	|     가장   첫 번째   글자를   대문자로   변경                                                	|
|                 s.title()               	|     문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환    	|
|                 s.upper()               	|     모두   대문자로 변경                                                                     	|
|                 s.lower()               	|     모두   소문자로 변경                                                                     	|
|               s.swapcase()              	|     대↔소문자 서로 변경                                                                      	|

#### .replace(old, new[, count])
```python
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!

```
#### .strip([chars])
```python
text = '    Hello, world!   '
new_text = text.strip()
print(new_text) # Hello, world!
```
#### .split(sep = None, maxsplit=-1)
```python
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!']
```
#### 'seperator'.join(iterable)
```python
words = ['Hello', 'world!']
text = '-'.join(words)
print(text) # Hello-world!
```
> 메서드는 이어서 사용 가능

## 리스트

### 리스트 값 추가 및 삭제 메서드
|          메서드         	|                                                   설명                                                  	|
|:-----------------------:	|:-------------------------------------------------------------------------------------------------------:	|
|        L.append(x)      	|     리스트   마지막에 항목 x를   추가                                                                   	|
|        L.extend(m)      	|     Iterable m의   모든 항목들을 리스트 끝에 추가 (+=과   같은 기능)                                    	|
|     L.insert(i,   x)    	|     리스트   인덱스 i에 항목 x를 삽입                                                                   	|
|        L.remove(x)      	|     리스트   가장 왼쪽에 있는 항목(첫 번째)   x를   제거     항목이 존재하지 않을 경우,   ValueError    	|
|          L.pop()        	|     리스트   가장 오른쪽에 있는 항목(마지막)을   반환 후 제거                                           	|
|         L.pop(i)        	|     리스트의 인덱스 i에   있는 항목을 반환 후 제거                                                      	|
|         L.clear()       	|     리스트의 모든 항목 삭제                                                                             	|

#### .append(x)
```python
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

```
#### .extend(iterable)
```python
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

```
#### .insert(i, x)
```python
# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)    
print(my_list) # [1, 5, 2, 3]
```
#### .remove(x)
```python
# remove
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)
```
#### .pop(i)
```python
# pop(i)
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]
```
#### .clear()
```python
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []

```


### 리스트 탐색 및 정렬 메서드
|               문법              	|                                   설명                                 	|
|:-------------------------------:	|:----------------------------------------------------------------------:	|
|     L.index(x,   start, end)    	|     리스트에   있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환    	|
|            L.reverse()          	|     리스트의 순서를 역순으로 변경 (정렬 X)|
|             L.sort()            	|     리스트를 정렬 (매개변수   이용가능)                                	|
|            L.count(x)           	|     리스트에서 항목   x의 개수를 반환                                  	|

#### L.index(x, start, end)
```
# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

```
#### L.reverse()  
```
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list) # [9, 1, 8, 2, 3, 1]
```
#### L.sort()       
```
# sort
my_list = [1, 2, 3]
my_list.sort()
print(my_list) # [1, 2, 3]

#내림차순
my_list.sort(reverse=True)
print(my_list) # [3, 2, 1]

```
#### L.count(x) 
```
# count
my_list = [1, 2, 3]
count = my_list.count(3)
print(count) # 3

```


# 복사
## 데이터 타입과 복사
- 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
- '변경 가능한 데이터 타입'과 '변경 불가능한 데이터 타입'을 다르게 다룸

## 복사유형
### 할당
- 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
```python
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) # [1, 2, 3][1, 2, 3]

copy_list[0] = 'hi'
print(original_list, copy_list) # ['hi', 2, 3] ['hi', 2, 3]
```


### 얕은 복사
- 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
```python 
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]

b[0] = 100
print(a, b) # [1, 2, 3] [100, 2, 3]

```
#### 얕은 복사의 한계
- 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우
- a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨
```python
a = [1, 2, [1, 2]]
b = a[:]
print(a, b) # [1, 2, [1, 2]]  [1, 2, [1, 2]]

b[2][0] = 100
print(a, b) # [1, 2, [100, 2]]  [1, 2, [100, 2]]
```
### 깊은 복사
```python
import copy


original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list) # [1, 2, [1, 2]]
print(deep_copied_list) # [1, 2, [100, 2]]

```
# 참고
### 문자열에 포함된 문자들의 유형을 판별하는 메서드(외우는거아님)
- isdecimal()
- isdigit()
- isnumeric()

# 보충
### 자료구조 needs
- 한 개의 변수에 여러개를 넣고싶음
- 근데 못넣어 왜 why? 메모리에는 하나밖에 못 넣음
- 그래서 주소 값 하나를 넣어놓은거

### method
- 객체 안의 함수
- 함수가 더 큰 개념이에요
- 혼용하는 경우가 많긴해요

### 
```python
a = 1 #원시값, Immutable Data type
b = a #Refrence type(참조값), Mutable Data type
print(a, b) # 1, 1
a = 10
print(a, b) # 10, 1

```


### 얕은 복사 / 깊은 복사
- 원시값은 스택에 저장되어있음
- 힙에는 원시값의 주소가 저장되어있음
- 참조값 안에 참조값을 넣게되면 얕은복사 이슈가 발생할 수 있음
- 해결하기 위해 깊은 복사 쓰면됨~
- 힙에있는 객체 내부의 원시값도 stack에 있음, 힙에 객체에는 원시값의 주소만있대

#### 얕은복사
![Shallow Copy](https://github.com/daegi0923/daegi0923/assets/156268579/4881f401-e766-43ac-be17-f28bd1867c47)


#### 깊은복사
![Deep Copy](https://github.com/daegi0923/daegi0923/assets/156268579/7e135297-0b1f-4104-910c-0a571783640b)


## Truthy / Falsy
```python
print(not '') # True
print(not 'True') # False
print(not '0') # False
```


## enumerate
- 순회가능한 객체에서 인덱스와 값을 반환하는 함수
- 근데 인덱스와 값 없어도 출력은 나옴(선택사항)
    - 한 개만 있으면 튜플로 나옴 ㅇㅇ ㅋ

## dictionary 와 in
- 딕셔너리에서 in은 key를 기준으로 작성함~~~~~~ㅜㅜ
```python
my_dict = {'apple' : 1, 'banana' : 2, 'cherry' : 3}
result = 1 in my_dict
print(result) # False

```