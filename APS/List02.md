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


---
# 240201
# 검색

## 순차 검색(Sequential Search)

- 가장 간단하고 직관적
- 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
    - 단순하여 구현이 쉬움, But 검색 대상의 수가 많은 경우에는 비효율적

### 정렬되어있지 않은 경우

1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾음
2. 찾으면 원소의 인덱스 반환
3. 자료구조의 마지막 까지 찾지 못하면 검색 실패
- 찾고자 하는 원소의 순서에 따라 비교회수 결정
- 시간 복잡도 : O(n)

### 정렬되어 있는 경우

- 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다느 ㄴ것이므로 더 이상 검색하지 않고 검색을 종료한다.
- 실패 반환하는 경우 평균 비교회수가 반으로 줄어듦
- 시간 복잡도 : O(n)

## Binary Search (이진 검색)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 이진 검색을 하기 위해서는 자료가 **정렬된 상태**여야 함

### 검색 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색 수행, 크다면 오른쪽 반에 대해 검색
- 찾을때 까지 반복

![binary-search-sequence-search](https://github.com/daegi0923/daegi0923/assets/156268579/0fea2891-9d1d-4622-822c-3bb134688084)

### 구현

- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
- 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업 필요

```python
def binary_search(target, data):
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return
```

## Selection Sort(선택 정렬)

### 인덱스

- DB에서 유래됨, 테이블에 대한 동작 속도를 높여주는 자료 구조
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다

### 배열을 사용한 인덱스

- 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없음
- 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스 사용

### 선택 정렬

![selection_sort](https://github.com/daegi0923/daegi0923/assets/156268579/3cbd468b-c36e-4e86-9ae7-e380bc852913)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬과정
    1. 주어진 리스트 중에서 최소값을 찾는다.
    2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
    3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
- 시간 복잡도 : O(n^2)

```python
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]\
# if 문 안쓰는 이유 -> if 문 쓰면 연산횟수 늘어남 (비교, 교환)
```

## Selection Algorithm

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 선택 과정
    1. 정렬 알고리즘을 이용하여 자료 정렬
    2. 원하는 순서에 있는 원소 가져오기

## 정렬 알고리즘 비교

![sort_algorithms](https://d2.naver.com/content/images/2020/01/img.png)

- 카운팅 정렬
    - 평균 :  O(n+k), 최악 : O(n+k)
    - 정수일때만, k가 비교적 작을 때만 가능