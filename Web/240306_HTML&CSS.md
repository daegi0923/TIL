# 240306_HTML&CSS
# 웹
### World Wide Web
- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
### Web
- Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
### Web site
- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
### Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진, "Web site"를 구성하는 하나의 요소
### Web page 구성요소
- Web page
    1. HTML : "Structure"
    1. CSS : "Styling"
    1. Javascript : "Behavior"
# 웹 구조화
## HTML
- HyperText Markup Language
- 웹 페이지의 **의미**와 **구조**를 정의하는 언어
### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- ex) HTML, Markdown
## HTML 구조
![HTML Structure](https://github.com/daegi0923/daegi0923/assets/156268579/72647148-bb1a-4297-9264-b42670a064d4)
- \<!DOCTYPE html\>
    - 해당 문서가 html로 문서라는 것을 나타냄
- \<html></html\>
    - 전체 페이지의 콘텐츠를 포함
- \<title></title\>
    - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- \<head>\</head>
    - HTML 문서에 관련된 설명, 설정 등
    - 사용자에게 보이지 않음    
- \<body>\</body>
    - 페이지에 표시되는 모든 콘텐츠
### HTML Element(요소)
![HTML Element](https://github.com/daegi0923/daegi0923/assets/156268579/3ace3d02-036b-4575-886e-affed73fb787)
- 하나의 요소는 여는 태그오 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재
### HTML Attiributes(속성)
![HTML Attribute](https://github.com/daegi0923/daegi0923/assets/156268579/6076d763-4db6-47f4-8e51-b063cc082270)

- 규칙
    - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야함
- 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

- image 태그는 닫는 태그가 없음 ㄷㄷ -->
- 닫는 태그가 없다 : 컨텐츠가 없다. 이미지 자체가 컨텐츠
- 속성 값만 있대
- alt -> 이미지가 없을 때 대체 텍스트 뭐 나올건지, 스크린 리더가 - - - 이미지를 만나면 alt값을 읽는대
## Text Structure
### HTMl Text structure
- HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것
### HTML
- 웹 페이지의 **의미**와 구조를 정의하는 언어
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것
### 대표적인 HTMl Text structure
- Heading & Paragraphs
    - h1~6, p
- List
    - ol, ul, li
- Emphasis & Importance
    - em, strong

#### MDN 문서
- [MDN](https://developer.mozilla.org/ko/)
- 웹에 관련된 걸 찾아볼 때는 MDN 키워드 넣어서 참고하면서 찾아보세욧!

---

# CSS
## CSS
- Cascading Style Sheet
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 구문
![CSS](https://github.com/daegi0923/daegi0923/assets/156268579/2c474ca0-420c-4782-ba66-a0e0ea9524cc)
- 선언이 끝나면 세미콜론(;)를 작성해 줘야함!
### CSS 적용 방법
1. 인라인(Inline) 스타일
    - HTML 요소 안에 style 속성 값으로 작성
1. 내부(Internal) 스타일 시트
    - head 태그 안에 style 태그에 작성
1. 외부(External) 스타일 시트
    - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

## CSS 선택자
### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
### CSS Selectors 종류
- 기본 선택자
    - 전체("*") 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자
    - 아이디(id) 선택자
    - 속성(attr) 선택자 등
- 결합자(Combinators)
    - 자손 결합자(" "(space))
    - 자식 결합자(">")


## 명시도
### Specificity(명시도)
- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
    - 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨
- CSS는 Cascading Style Sheet
- Cascade : 계단식
- 한 요소에 동일한 가중치를 가진 선택자가 적용될 때, CSS에서 마지막에 나오는 선언이 사용됨
### 명시도 적용 예시
- 동일한 h1 태그에 다음과 같이 스타일이 작성된다면 h1 태그 내용의 색은 red가 적용됨
![specificity](https://github.com/daegi0923/daegi0923/assets/156268579/7eb2f42f-e91a-4f35-8334-903ec445b704)
### 명시도가 높은 순
1. Importance
    - !important
1. Inline 스타일
1. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
1. 소스 코드 선언 순서

### \!important
- 다른 우선순위 규칙보다 우선하여 적용하는 키워드
> Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음

### 속성은 되도록 'class'만 사용할 것!
- id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
- 문서에서 단 한번 유일하게 적용될 스타일의 경우에만 "id 선택자" 사용을 고려

## CSS 상속
- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
### CSS 속성 2가지 분류
- 상속 되는 속성
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
    - Box model 관련 요소(width, height, border, box-sizing ...)
    - position 관련 요소(position, top/right/bottom/left, z-index) 등...
### CSS 속성 상속 여부는 MDN문서에서 확인해라잇


---
## 참고
### HTML 관련 사항
- 요소(태그) 이름은 대소문자를 구분하지 않지만 "소문자" 사용을 권장
- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 "큰 따옴표" 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의
