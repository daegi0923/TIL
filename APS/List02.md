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