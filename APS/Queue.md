# Queue
## Queue
- 선입선출 구조(FIFO : First In First Out)
- 큐의 뒤에서는 삽입만, 큐의 앞에서는 삭제만
- 선형 자료 구조

### 큐의 선입선출 구조
![FIFO](https://github.com/daegi0923/daegi0923/assets/156268579/34c6a518-d013-4c20-a085-46d6a84b14e7)

### 큐의 기본 연산
- 삽입 : enQueue
- 삭제 : deQueue
![Queue](https://github.com/daegi0923/daegi0923/assets/156268579/25df80f5-646c-4431-8a77-c93fc9df7922)

## 원형 큐
- 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
### 원형 큐의 구조
- 초기 공백 상태
    - front = rear = 0
- Index의 순환
    - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
    - 나머지 연산자 mod 사용
- front 변수
    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입위치 및 삭제 위치

||삽입 위치|삭제 위치|
|---|---|---|
|선형큐|rear = rear + 1| front = front + 1|
|원형큐|rear = (rear +1)mod n| front = (front+1) mod n|

## 연결 큐
### Linked List를 이용한 큐
- 큐의 원소 : Node
- 큐의 원소 순서 : Node 의 연결 순서, Linked
- front : 첫 번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크

### 상태 표현
- 초기 상태 : front == rear == null
- 공백 상태 : front == rear == null
![LinkedList](https://github.com/daegi0923/daegi0923/assets/156268579/843d8a24-4bc1-4b05-adb4-7685ae822182)

## Priority Queue
### 우선순위 큐의 특성
- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 가 아닌 우선순위가 높은 순서대로 나감

## 버퍼(Buffer)
### 버퍼
- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
### 버퍼의 자료 구조
- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
- FIFO 방식의 큐가 활용됨



---
# 240216
## BFS
- 그래프를 탐색하는 방법
    - DFS(Depth First Search)
    - BFS(Breadth First Search)
- BFS : 탐색 시작점의 인접한 정점들을 차례로 방문, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
