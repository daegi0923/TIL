# 240118 - 모듈

# 모듈 (Module)

- 한 파일로 묶인 변수와 함수의 모음
- 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

### 모듈 예시

- 파이썬 math 모듈
- 수학 관련 변수와 함수가 작성된 모듈
- 참고 문서 : https://docs.python.org/3/library/math.html

```python
import math

print(math.pi)
print(math.sqrt(4))
```

## 모듈 활용

### 모듈 가져오기

- 모듈 사용하려면 import 필요

```python
import math
```

- help 함수를 통해 모듈에 무엇이 들어있는지 확인 가능

```python
help(math)
```

### 모듈 사용하기

- **‘.(dot)’** → 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라 라는 의미의 연산자

### 모듈을 import하는 다른 방법

- from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시

```python
from math import pi, sqrt
```

### 모듈 주의사항

- 만약 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
- 마지막에 import된 이름으로 대체됨

```python
# 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음
from math import *
```

### 사용자 정의 모듈

```python
# my_math.py
def add(x, y):
    return x + y
```

```python
# test.py
from my_math import add 

print(add(5, 5))
```

# 파이썬 표준 라이브러리(Python Standard Library)

- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음
- 참고 문서 : https://docs.python.org/ko/3/library/index.html

## 패키지 Package

- 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것 (.py → 모듈, 디렉토리 → 패키지)
- 모듈 < 패키지 < 라이브러리

### 패키지 사용하기

- 아래와 같은 디렉토리 구조로 작성
- 패키지 3개 : my_package, math, statistics
- 모듈 2개 : my_math, tools
- 디렉토리 전체 구조
    
    ```markdown
    📦...
     ┣ 📜sample.py
     ┣ 📂my_package
     ┃ ┣ 📂math
     ┃ ┃ ┗ 📜my_math.py
     ┃ ┣ 📂statistics
     ┃ ┃ ┗ 📜tools.py
    
    ```
    

https://github.com/ragu6963/TIL/assets/32388270/01f0ca51-45b2-4468-8a38-b81c6db14b24

- 각 패키지의 모듈을 import 하여 사용하기
    
    ```python
    # sample.py
    
    from my_package.math import my_math
    from my_package.statistics import tools
    
    print(my_math.add(1, 2))  # 3
    print(tools.mod(1, 2))  # 1
    
    ```
    

### PSL 내부 패키지

- 설치 없이 바로 import하여 사용

### 외부 패키지

- pip를 사용하여 설치 후 import 필요

### pip `파이썬 패키지 관리자`

- 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치

> https://pypi.org/
> 

### 패키지 설치

- 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음
    
    ```bash
    $ pip install SomePackage
    $ pip install SomePackage==1.0.5
    $ pip install SomePackage>=1.0.4
    ```
    

### requests 외부 패키지 설치 및 사용 예시

```bash
$ pip install requests

```

```python
import requests

url = '<https://random-data-api.com/api/v2/users>'
response = requests.get(url).json()

print(response)

```

### 패키지 사용 목적

모듈들의 이름공간은 구분하여 충돌을 방지 
모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

---

# 제어문 Control Statement

- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

## 조건문 (Conditional Statement)

- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

### ‘if’ statement

- if statement의 기본 구조
    
    ```python
    if 표현식:
        코드 블록
    elif 표현식:
        코드 블록
    else:
        코드 블록
    ```
    

## 반복문 (Loop Statement)

### ‘for’ statement

- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
- for statement의 기본 구조
    
    ```python
    for 변수 in 반복 가능한 객체:
        코드 블록
    ```
    

### iterable

- 반복 가능한 객체
- 반복문에서 순회할 수 있음
- 시퀀스 객체 뿐만 아니라 dict, set 등도 포함

### 딕셔너리 순회

- dict에서 key값만 순회함
- value를 조회하려면 key를 이용해서 조회

```python
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}
for key in my_dict:
    print(key)
    print(my_dict[key])
```

### 인덱스로 리스트 순회

- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
    
    ```python
    numbers = [4, 6, 10, -8, 5]
    
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    
    print(numbers) # [8, 12, 20, -16, 10
    ```
    

### ‘while’ statement

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행<br>
== 조건식이 거짓(False)가 될 때 까지 반복
- while statement의 기본 구조
    
    ```python
    while 조건식:
        코드 블록
    ```
    
- **while 문은 반드시 종료 조건이 필요!**

### ‘while’ statement

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
== 조건식이 거짓(False)가 될 때 까지 반복

### 적절한 반복문 활용하기

- for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때
- while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

---

# 반복제어

- **break** : 반복을 즉시 중지
- **continue** : 다음 반복으로 건너뜀

### break 예시

- 프로그램 종료 조건 만들기
    
    ```python
    number = int(input('양의 정수를 입력해주세요.: '))
    
    while number <= 0:
        """
        종료 조건과 break
        """
        if number == -9999:
            print('프로그램을 종료합니다.')
            break
    
        if number < 0:
            print('음수를 입력했습니다.')
        else:
            print('0은 양의 정수가 아닙니다.')
    
        number = int(input('양의 정수를 입력해주세요.: '))
    
    print('잘했습니다!')
    
    """
    양의 정수를 입력해주세요.: -9999
    프로그램을 종료합니다.
    잘했습니다!
    """
    
    ```
    
- 리스트에서 홀수만 출력하기
    
    ```python
    numbers = [1, 3, 5, 6, 7, 9, 10, 11]
    found_even = False
    
    for num in numbers:
        if num % 2 == 0:
            print('첫 번째 짝수를 찾았습니다:', num)
            found_even = True
            break
    
    if not found_even:
        print('짝수를 찾지 못했습니다')
    
    """
    첫 번째 짝수를 찾았습니다: 6
    """
    
    ```
    

### continue 예시

- 리스트에서 홀수만 출력하기

> **현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감**
> 


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

"""
1
3
5
7
9
"""
```



### break와 continue 주의사항

- break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
- 특정한 종료 조건을 만들어 break을 대신하거나,if 문을 사용해 continue 처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요
- 수정 전
    
    ```python
    for number in range(1, 5):
        if number == 3:
            continue
        print(number)
    """
    1
    2
    4
    """
    
    ```
    
- 수정 후
    
    ```python
    for number in range(1, 5):
        if number != 3:
            print(number)
    """
    1
    2
    4
    """
    
    ```
    

# 참고

## List Comprehension

- 간결하고 효율적인 리스트 생성 방법
    
    

### List Comprehension 구조

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

### List Comprehension 예제

```python
[str(n) for n in [8, 16, 18, 19, 12, 1, 6, 7]]

# ['8', '16', '18', '19', '12', '1', '6', '7']
```

```python
[n for n in [8, 16, 18, 19, 12, 1, 6, 7] if n % 2 == 0]
# [8, 16, 18, 12, 6]
```

### Comprehension을 남용하지 말자.

> "Simple is better than complex"
"Keep it simple, stupid"
> 

## pass

- 아무런 동작도 수행하지 않고 넘어가는 역할

> 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용
> 

## enumerate(iterable, start=0)

- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
print(f'인덱스 {index}: {fruit}')

"""
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
"""
```

---

# 보충

## iterable objects

- 내부적으로 ‘__iter__’와 ‘__next__’가 구현되어 있음.