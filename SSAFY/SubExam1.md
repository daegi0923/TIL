## 과목평가 대비
### 과목평가
* 32문제 객관식20 단답10 서술2
* 이론위주
### 월말평가
* 코드로 작성

#### 언패킹
```python
a = [1, 2, 3, 4, 5]
b, c, *d = a
print(d)
```

```python
def func(*args):
    print(args)

func([1, 2, 3])  # (1, 2, 3)
```
#### 리스트 vs 튜플
* 가변 vs 불변
* 함수는 같은 값을 넣으면 같은 결과가 나와야함 -> 튜플
* 변수 언패킹하면 리스트 -> 상관없으니깐~ 변수는 값을 참조하는게 계속 바뀜


#### List Comprehension
```python
[5, 5, 5, 5, 5] #Hard coding
lst = [5 for _ in range(5)]
```

#### not
* not : 뒤집는 연산자
* 1 => truthy
* False => falsy
```python
print(not 1) # False
print(not False) # True
print(not 0) # True

```
* truthy/falsy 한거 구분해라

#### 반복문
```python
for i in "hello":
    print(i)
```

#### 인덱싱
```python
a = [['hello', 2], [3, 4]]
print(a[0])
print(a[0][0])
print(a[0][0][2])

```
#### 연산자 우선순위
1+1*1**1-1 = ?
#### 시퀀스타입 종류
list, tuple, range
#### 논 시퀀스 타입?

#### enumerate
for i in enumerate(lst):
    print(?, x)

1. enumerate 사용법
2. enumerate 정의

#### 함수 파라미터
def func(a, *b, **c)
func(?????)
어떤식으로 들어가는지~

#### Slicing
lst = [1, 2, 3]
lst[1:2] #lst[0:n-1] 왜 인덱스는 0번부터 시작하는가?

#### 함수
def a(n, n2):
    return n+n2
b = a(1, 2) + a(1, 2) #이거 해보삼
print(a(1, 2), a(1, 2))

#### dict
dic = {
    '1' :

}
for i in dic:
    print(dic)
딕셔너리 순회되는지 enumerate 되는지

#### 비교연산자
x = 1
y = 2
print(x > y)

#### 모듈
python -> 모듈 만들려면 확장자 ?

#### pass
pass 역할

#### 재귀함수
어떤식으로 동작하는지 공부해와~

#### type 변환
1 + '1'
1 + 0.1

#### 조건문
조건문 코드 예시 -> 어떤거 출력하니~
hint 44p보세요 복수조건문
#### range
[range(3), range(3)]
[[1, 2, 3], [1, 2, 3]]
map(lambda x, y : x + y , *lst) #뭐가 나올까?

#### map
['1', '2', '3'] -> [1, 2, 3] 바꿀려면 어떻게 할건데? 빈칸문제로

#### 논리연산자 and or
print(0 and 1)
print(0 or 1)

#### 모듈 import
tqewtqwt -> test.py
a.py로 가져올려면? 뭐해야되는데
hint : 수입하다

#### 반복문
for , while 어떤때 쓴다 고민해바
~한 상황에서 쓸 반복문을 고르세요

#### 이중 for문
as = [1, 2]
bs = [3, 4]
cs = [5, 6]
for a in as:
    for b in bs:
        for c in cs:
            print(a, b)

#### return 없는 함수
def a():
    pass

print(a()) -> 뭐가 출력되는데? return문 없을때
공부 ㄱ

####
a = 2
새로운 변수를 만들지 않고 5제곱하는 코드 작성

#### Slicing
[1:2]

#### Scope
LEGB관련 공부(단답식)

### 서술형
1. Type변환
print(1 + '1')
print(1 + 0.1)
print(1 + [])
print({} + [])
서로 다른 데이터 타입이 있을때 결과와 그렇게 되는 이유
파이썬에서는 정수와 문자열의 연산자를 지원하지 않음 자동 형변환 x

2. 패킹, 언패킹
a = range(1, 11)
print(a)

a에 있는 요소를 확인하려면 어떻게 해야하는가? 서술형임 ㅋ
