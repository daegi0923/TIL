# 240220 Tree

## Tree
- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장


### Tree - defination
- 한개 이상의 노드로 이루어진 유한집합
    - 노드 중 최상위 노드를 루트(root)라 함
    - 나머지 노드들은 n 개의 분리 집합 T1, ..., Tn으로 분리 가능
- T1, ..., Tn은 하나의 트리가 됨 -> 루트의 subtree라 함

### Tree - expression
- node : 트리의 원소
- edge : 노드를 연결하는 선, 부모 노드와 자식 노드를 연결
- root node : 트리의 시작 노드 
- sibling node : 같은 부모 노드의 자식 노드 들
- 조상 노드 : edge를 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- subtree : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
- 차수(degree)
    - 노드의 차수 : 노드에 연결된 자식 노드의 수
    - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
    - 단말 노드(leaf node) : 차수가 0인 노드, 자식 노드가 없는 노드
- 높이(level)
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
    - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨
![tree](https://github.com/daegi0923/daegi0923/assets/156268579/0a5f177d-4de9-4010-a3c1-0599c4a5788b)

## 이진트리
- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
    - 왼쪽 자식 노드(left child node)
    - 오른쪽 자식 노드(right child node)

### 이진트리 - charactristic
- 레벨 i에서 노드의 최대 개수는 2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2^(h+1)-1)개가 된다.

### 포화 이진 트리(Full Binary Tree)
- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
    - 높이 3일 때 2^(3+1) = 15개의 노드
- 루트를 1번으로 하여 (2^(h+1)-1)까지 정해진 위치에 대한 노드 번호를 가짐
![Full Binary Tree](https://github.com/daegi0923/daegi0923/assets/156268579/18600b46-ccac-4191-b78e-6bfd29b0ab65)

### 완전 이진 트리(Complete Binary Tree)
- 높이가 h이고 노드 수가 n개 일 때(단, 2^h <= n<= 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번 부터 n번 까지 빈 자리가 없는 이진 트리
- ex) 노드가 10개인 완전 이진 트리
![Complete Binary Tree](https://github.com/daegi0923/daegi0923/assets/156268579/acf5e471-ed0b-4213-a4d9-982ac8568e73)

### 이진 트리 - 순회(traversal)
- 순회(traversal) : 트리의 각 노드를 중복되지 않게 전부 방문하는 것
- 3가지의 기본적인 순회 방법
    1. 전위순회(preorder traversal) : VLR
        - 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문
    1. 중위순회(inorder traversal) : LVR
        - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
    1. 후위순회(postorder traversal) : LRV
        - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문


---
### null, none, undefined
- null : 명시적 부재
- none : 암묵적 부재, 암시적 부재
- undefined : 암묵적 부재 => javascript

### 파이썬에서 리스트 전역변수로 호출 안해도 되는 이유
(https://medium.com/@dltkddud4403/python-%EC%A7%80%EC%97%AD%EB%B3%80%EC%88%98-%EC%A0%84%EC%97%AD%EB%B3%80%EC%88%98-%EA%B4%80%EB%A0%A8-%EA%B0%9C%EB%85%90-4ea2a1865071)
(https://velog.io/@tenacious_mzzz/python-%EC%A0%84%EC%97%AD%EB%B3%80%EC%88%98-%EB%B0%B0%EC%97%B4)

---
# 240221
