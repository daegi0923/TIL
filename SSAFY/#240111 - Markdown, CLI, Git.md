# Markdown

# Markdown

## 제목2

### 제목3

### 제목4

### 제목5

### 제목6

## 리스트

### 순서가 없는 리스트

- 점심메뉴
    - 라면
    - 김밥

### 순서가 있는 리스트

1. 부울경의 반 리스트
    1. 부울경 1반
    2. 부울경 2반

## Code block

```python
print("hello world")

```

요고는 리얼루다가 필수
코드 보낼 때 반드시 코드블록안에 담아보내세요!

## 링크 & 이미지

[google](https://www.google.com/)

## 텍스트 관련 문법

~~장난~~
**점심시간은 12:50 ~ 14:00**
*기울임*

## 수평선

- 하이픈 세개 이상 적으면 작동

---

---

## Markdown 가이드

- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

[예시 : 점심메뉴](https://www.notion.so/e5e16374f700445fa684d3dd050f3aaf?pvs=21)

# CLI

# CLI

- **.** (현재 디렉토리) / **..** (현재의 상위 디렉토리)
- 폴더 만들기 : **mkdir** (폴더이름)
- 경로 바꾸기(Change directory) : **cd** (폴더이름)
- 현재 폴더의 리스트 : **ls** (뒤에 슬래시 붙어있으면 폴더임)
    - ls -a
    - ls -al
- **pwd** : Print working directory(현재위치 파악)
- **touch** ccc.txt : ccc.txt 파일생성
- **cd ..** : 부모 폴더로 이동
    - **cd ../ ..** : 부모의 부모로 이동
- **rm (파일명)** : remove
    - **rm -(옵션)**
        1. 비어있지않은 폴더는 r 옵션 없이 삭제 불가
        2. f 옵션 : 강제로 파일/디렉토리 삭제 (ex  rm -rf)
- **start (파일명)** : 폴더/파일 열기
    - 파일명 치고 탭누르면 자동완성 ㅇㅇ



# Git

# **git** : 분산 버전 관리 시스템

- 백업과 복구에 용이

## Git의 3가지 영역

### Working Directory / Staging Area / Repository

---

## ⭐⭐⭐add commit push⭐⭐⭐

### add : 로컬 → 스테이지

### commit : 스테이지에 올라간 파일에 쪽지를 적는다

### push : 스테이지 → Repository

---

1. git **init** : 시작할때 초기화시킴
2. git **status** : 상태창!
3. git **add** (파일이름)
4. git **commit** -m “commit message”
5. git **remote add**
    - git remote add origin [https://github.com/사용자이름/저장소.git](https://github.com/%EC%82%AC%EC%9A%A9%EC%9E%90%EC%9D%B4%EB%A6%84/%EC%A0%80%EC%9E%A5%EC%86%8C.git)
    - origin ← 주소 별명임
6. git **log** : 로그 보기, commit 한 로그 확인가능
7. git **push** 
    - git push origin master:master

- **code .** 치면 현재위치 vscode로 열림!

1. **clone** : repos에 업로드 되어있다는 가정하에 repo 자체를 통으로 가져오는 것
2. **pull** : repo에 수정된 내용을 local에서 최신화

### Git으로 협업하려면…

- 회사 레포지토리(관리자 : 팀장) → 내 레포로 포크 딴 후 pull request 보내면된다
- 브랜치 만들어서 포크따서 응용하는 것도 가능!