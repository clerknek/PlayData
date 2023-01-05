# 모듈 버전을 저장하는 변수. 변수명: __version__
__version__ = 1.0

def greeting(name):
    return f"{name}님 안녕하세요"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"
    
# import 를 통해서 실행될 경우에는 아래 부분은 실행되면 안된다.
# python my_module.py 을 통해 실행될 경우에만 실행되어야 한다.

if __name__ == "__main__":
    print(__name__)
    g = greeting("김영수")
    p = Person("홍길동", 20)
    print(g)
    print(p)