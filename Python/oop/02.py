class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown

p2 = Person()
p2.name = 'kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)