# 클래스 정의
class Person:
    blood_color = 'red'

    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('nmixx')
singer2 = Person('aespa')

# 메서드 호출
print(singer1.singing())  # nmixx가 노래합니다.
print(singer2.singing())

# 속성(변수) 접근
print(singer1.blood_color)  # red
print(singer2.blood_color)  # red


