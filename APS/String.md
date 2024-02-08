# 문자열
## 문자의 표현
- ASCII(American Standard Code for Information Interchange)
- 문자 인코딩 표준

### 유니코드 인코딩(UTF : Unicode Transformation Format)
- UTF-8(in web)
    - Min : 8bit, Max : 32bit(1 Byte * 4)
- UTF-16(in windows, java)
    - Min : 16bit, Max : 32bit(2 Byte * 2)
- UTF-32(in unix)
    - Min : 32bit, Max : 32bit(4 Byte * 1)
    
## 문자열의 분류
>![image](https://github.com/daegi0923/daegi0923/assets/156268579/3945acfd-7bd6-4047-aa65-4e9a7b823d59)

### java에서 String 클래스에 대한 메모리 배치 예
- java.lang.String 클래스에는 기본적인 객체 메타 데이터 외에 hash, count, offset, value 의 필드를 포함
> ![String in java](https://github.com/daegi0923/daegi0923/assets/156268579/6e1ae76a-edf7-4fb8-8356-9a003897ca88)

```python 
import sys

a = ''
b = 'h'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
```

### C언어에서 문자열 처리
- 문자열은 문자들의 배열 형태로 구현된 응용 자료형
- 마지막에 끝을 표시하는 널문자('\0')을 넣어줘야함
g
### input()
```python
s1 = list(input())
s2 = input()
s1[0] = 'd'
print(s1)
print(s2[0])
s2[0] = 'a' #'str' object does not support item assignment
```

### Python 에서의 문자열 처리
- char 타입 없음
- 텍스트 데이터의 취급방법이 통일되어 이씅ㅁ
- 문자열 기호
'(홑따옴표), "(쌍따옴표), '''(홑따옴표 3개), """(쌍따옴표 3개)
+ `+`연결(Concatenation)
    - 문자열 + 문자열 : 이어 붙임
+ `*`반복
    - 문자열 * 수 : 수만큼 문자열 반복
- 문자열은 시퀀스 자료형으로 분류됨 -> 인덱싱, 슬라이싱 연산 사용가능
- 문자열 클래스에서 제공되는 메소드
    > replace(), split(), isalpha(), find()
- immutable : 값을 변경할 수 없음(튜플처럼~)

### 문자열 뒤집기
```python
s = 'Reverse this strings'
s = s[::-1]

s = 'abcd'
s = list(s)
s.reverse()
s = ''.join(s)
```

### 문자열 비교
- Java에서는 eqlals() 메소드 제공
    - == 연산은 메모리 참조가 같은지 묻는거
- 파이썬에서는 == 연산자와 is 연산자를 제공
    - == 연산자는 내부적으로 특수 메서드 __eq__()를 호출

- `is` 연산자 : 두 객체가 동일한 주소에 할당된 객체임을 비교
- `==` 연산자 : 값이 같은지를 비교
```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1, s2, s1 is s2) # True
print(s1, s3,s1 is s3) # False
print(s1, s4,s1 is s4) # True
print(s1, s5,s1 is s5) # False

print(s1, s2,s1 == s2) # True
print(s1, s3,s1 == s3) # False
print(s1, s4,s1 == s4) # True
print(s1, s5,s1 == s5) # True

```

### 문자열 숫자를 정수롷 변환하기

- java에서는 숫자 클래스의 parse 메소드 제공
    - ex) Integer.parseInt(String)
    - 역함수로 toStrint() 메소드 제공
- 파이썬에서는 문자와 문자변환 함수 제공
    - ex) int("123"), float("3.14"), str(123), repr(123)

### int()와 같은 atoi()함수 만들기
```python
def atoi(s):
    i = 0
    for digit, x in enumerate(s):
        i = i* 10 + (ord(x)-ord('0'))
    return i

s = '123'
a = atoi(s)
print(a+1)
```
- ord(x) : x에 해당하는 10진수 유니코드 반환
    - ord(x) - ord(0) : x의 유니코드에서 0의 유니코드를 뺀 값, 즉 x

### str()를 사용하지 않고, itoa() 구현
```python
def itoa(s):
    i = ""
    while True:
        i = chr(s%10+ord('0')) + i
        s = s//10
        if s == 0:
            break
    return i


num = 123
string = itoa(num)
print(string + 'hi')

```
- chr(x) : 10진수 유니코드 x에 해당하는 문자 반환
    - chr(x-ord('0')) : 문자열 x 반환!


# 240207_String02

# 패턴 매칭

## 고지식한 알고리즘(Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴내의 문자들을 일일이 비교
- 최악의 경우 시간 복잡도 : O(MN) → 안좋음

### 브루트 포스를 활용한 패턴매칭

```python
def f(pat, txt, M, N):
    for i in range(N-M+1): # text에서 비교 시작 위치
        for j in range(M):
            if txt[i+j] != pat[j]: # 불일치면 다음 시작위치로 가고
                break
        else: # for-else : for문이 모두 끝나면 실행되는 거임 ㅇㅇ
            # 패턴 매칭에 성공하면
            return 1
    # 모든 위치에서 비교가 끝난경우
    return 0

T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    ans = f(pat, txt, M, N)
    print(f'#{tc} {ans}')
```

## KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 무자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열  next[M]을 구해서 잘못된 시작을 최소화함
    - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
- 시간복잡도 : O(M+N)

### 아이디어 설명

- 텍스트에서 abcdabc 까지는 매치되고, e에서 실패한 상황 패턴의 맨 앞의 abc와 실패 직전의 abc는 동일함을 이용할 수 있다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3efa4bec-a626-4de9-89ed-a2a1b3da7df0/20338582-c6eb-474f-84ab-d4209c763cde/Untitled.png)

- 매칭이 실패했을 때 돌아갈 곳을 계산한다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3efa4bec-a626-4de9-89ed-a2a1b3da7df0/d46ac5eb-ff59-4b53-93b2-12984a6bef05/Untitled.png)

```python
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0 # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return

t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = "AAAAABAAABA"
p =  "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)
```

## 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 보이어-무어 알고리즘은 패턴에 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼이 된다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3efa4bec-a626-4de9-89ed-a2a1b3da7df0/c0f85d17-d92a-488d-ac65-429230309688/Untitled.png)

- 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재할 경우

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3efa4bec-a626-4de9-89ed-a2a1b3da7df0/7fd336df-2ca2-46a5-a821-211433458ddb/Untitled.png)

### 보이어-무어 알고리즘을 이용한 예

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/3efa4bec-a626-4de9-89ed-a2a1b3da7df0/b150b39c-d213-4c84-9f19-166bd09548aa/Untitled.png)

### 문자열 매칭 알고리즘 비교

- 패턴 길이 M, 문자열 길이 N
- 브루트포스 : O(MN)
- 카프-라빈 알고리즘 :  θ(N)
- KMP 알고리즘 : θ(N)
- 보이어-무어 알고리즘 : 최선의 경우 Omega(N)
    - 텍스트 문자를 다 보지 않아도 된다
    - 최악의 경우 : θ(MN)

### 3143_문자열에서 갯수 세기

```python
T = int(input())
for t in range(T):
    A, B = input().split()
    N = len(A)
    M = len(B)
    cnt = 0
    while True:
        if B not in A:
            result = len(A)
            break
        A = A.replace(B,'*')

    ans = N - (M-1)*cnt
    print(f'#{t+1} {result}')
```

---

파이썬 → 멀티패러다임 

함수형 프로그래밍, 일급객체의 조건, 고차함수

이게 뭔데 ㅋㅋㅋㅋ