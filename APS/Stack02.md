# Stack02
# 240213

## 계산기1
- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 계산식의 값을 계산가능
### 후위 표기식으로 변경
1. 토큰 하나 가져오기
1. 스택 연산 push()
    - 토큰이 연산자면 스택 top과 비교
    - 높으면 push
    - 여는 괄호 push
1. top 변경
    - 스택에 쌓여 있는 마지막 값을 가리킴
1. 피연산자면 출력
1. 닫는 괄호 만나면
    1. 여는 괄호를 만날 때 까지 모두 pop()

## 계산기2
### 후위 표기법의 수식을 스택을 이용하여 계산
1. 피연산자를 만나면 스택에 push
1. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 qush
1. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

```python
# (6+5*(2-8)/2)
top = -1
stack = [0] * 100

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 안에서의 우선순위

fx = '(6+5*(2-8)/2)'
postfix = ''

for tk in fx:
    # 여는 괄호 push, 연산자이고 top 원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]]< isp[tk]):
        top += 1
        stack[top] = tk
    elif tk in '*/+-' and isp[stack[top]]>= isp[tk]: # 연산자이고 top 원소보다 우선순위가 높지 않으면
        # top 원소의 우선순위가 낮을 때까지 pop
        while isp[stack[top]]>= isp[tk]:
            top = top - 1
            postfix = postfix + stack[top+1]
        # push
        top = top + 1
        stack[top] = tk
    elif tk == ')': # 닫는 괄호면, 여는 괄호를 만날 때 까지 pop
        while stack[top] != '(':
            top = top - 1
            postfix = postfix + stack[top+1]
        top = top - 1 # 여는 괄호 pop해서 버려
        stack[top + 1]
    else: #피연산자인 경우
        postfix = postfix + tk
print(postfix)
```

## 백트래킹
- 해를 찾는 도중에 '막히면'(즉, 해가 아니면) 되돌아가서 다시 해를 찾는 방법
- 최적화(optimization)문제와 결정(decision) 문제를 해결할 수 있다.
- 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes'또는 'no'로 답하는 문제

### 백트래킹과 깊이우선탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임.(Prunning 가지치기)
- 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우 여전히 O(N^2)를 요함
- 모든 후보를 검사하지 않음!

### 백트래킹 기법
- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

### 백트래킹의 절차
1. 상태 공간 트리의 깊이 우선 검색을 실시
2. 각 노드가 유망한지 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

## 부분집합
- PowerSet : 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
- 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2**n 개 이다.
### 백트래킹 기법을 이용한 powerset
- n개의 원소가 들어있는 집합의 2**n개의 부분집합을 만들 때, true 또는 false 값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용.
- 배열의 i번째 항목은 i번째 원소가 부분집합의 값인지 아닌지 나타내는 값

```python
def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1, k)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)


N = 4
arr = [1, 2, 3, 4]
bit = [0] * N
f(0, N)
```


## 분할정복
- Divide, Conquer, Combine
- 퀵소트, 머지소트 <- 이거 두개는 꼭 알아
### 병합 정렬
![MergeSort](https://github.com/daegi0923/daegi0923/assets/156268579/e1da1b28-d2cc-4afb-a662-8ec6b090e1e7)

### 퀵 정렬
- Keyword
    1. Pivot
    1. Divide and Conquer
    1. vs Merge Sort

- 최악의 경우(Worst cases) : T(n) = O(n^2)
    - 최악의 경우는 정렬하고자 하는 배열이 오름차순 정렬되어있거나 내림차순 정렬되어있는 경우다.
    - 작은 값 큰 값을 계속 피봇으로 정했을때도 
![QuickSort](https://github.com/daegi0923/daegi0923/assets/156268579/54a16df6-e72f-4aa6-ba5b-df4e6d00f5e1)

### Quick Sort vs Merge Sort
![QvsM](https://github.com/daegi0923/daegi0923/assets/156268579/37fa3e14-1828-4e47-9c50-193ca8a2ac62)

---
# Queue
- 단독으로는 안나옴, 스택이랑 비교 또는 응용해서 알고리즘
- 큐를 사용하지 않고 큐를 구현? -> 스택 2개 ㄱ

### 컴퓨터가 음수를 표현하는 방식
1. 부호 절대값
1. 1의 보수
1. 2의 보수
- 요즘은 2의 보수 쓴대 ㅋㅋ