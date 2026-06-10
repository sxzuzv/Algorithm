# 클래스
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("안녕하세요! 저는", self.name, "입니다.")

kuri = Person("쿠리")
kuri.talk()

haem = Person("햄햄")
haem.talk()