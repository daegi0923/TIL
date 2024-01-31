# 240131_List02_1

# 2차원 배열

## 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```python
N = int(input())
lst = [list(map(int, input().split()) for _ in range(N)]
# 3
# 1 2 3
# 4 5 6 
# 7 8 9 
N = int(input())
lst = [list(map(int, input()) for _ in range(N)]
# 3
# 123
# 456
# 789
lst2 = [[0]*N]*N
lst2[0][0] = 1
# 하나만 변해야되는데 세개 다 변함
# 얕은복사니깐 쓰지마세요 ㅡㅡ
```

## 2차원 배열의 접근
### 배열 순회
- n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
### 행 우선 순회
![행우선순회](https://github.com/daegi0923/daegi0923/assets/156268579/29eb5f2b-f0c4-4863-a8ad-c556a98aa4f3)

```python
for i in range(n):
    for j in range(m):
        f(array[i][j])
        ## r, c / p, q 등 사용하세요 i, j/x, y는 아껴라~ ㅋ
```
### 열 우선 순회
![열우선순회](https://github.com/daegi0923/daegi0923/assets/156268579/8826d903-ced2-40cd-9d76-9b106fcfb877)

```python
for j in range(m):
    for i in range(n):
        f(array[i][j])
```

### 지그재그 순회
![지그재그순회](https://github.com/daegi0923/daegi0923/assets/156268579/92b893c9-b381-43cd-83e6-654fdc950337)
```python
for j in range(m):
    for i in range(n):
        f(array[i][j + (m - 1 - j*2)* (i%2)])
```

### 델타를 이용한 2차 배열 탐색
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 인덱스 (i, j)인 칸의 상하좌우 칸 (ni, nj)

```python
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

i = 3
j = 4
for k in range(4):
    ni = i + di[k]
    nj = j + kj[k]
    print(ni, nj)
```

### 전치 행렬
![전치행렬](https://github.com/daegi0923/daegi0923/assets/156268579/cf3c56c8-3216-4228-98b6-7086602d8e21)
```python
for i in range(n):
    for j in range(m):
        if i < j:
            arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]
```
# 부분 집합 합 문제
- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
## 부분집합 생성하기
- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.
## 비트 연산자
- 8 bit == 1 byte
- 숫자를 저장할 때 메모리에서는 이진수로 저장 (5 -> 00101)

### 비트 연산자
- `&` : 비트 단위로 AND 연산
- `|` : 비트 단위로 OR 연산
- `<<` : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
- `>>` : 피연산자의 비트 열을 오른쪽으로 이동시킨다.

### << 연산자
- 1 << n : 2^n, 비트를 왼쪽으로 n칸 shift, 원소가 n개일 경우 모든 부분집합의 수를 의미
### & 연산자
- i&(1<<j) : i의 j번째 비트가 1인지 아닌지를 검사
### 예제 : 부분집합 구하기
```python
lst = [3, 6, 7, 1, 5, 4]

n = len(lst) # n : 원소의 개수

for i in range(1, 1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1<<j): # i의 j번 비트가 1인경우
            print(lst[j], end = ", ") # j번 원소 출력
    print()
print()
```