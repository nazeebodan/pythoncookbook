'''
Created on 2017年7月16日

@author: suredandan
'''


def Tracer(aClass):
    #     print(dir(object))

    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)

        def __getattr__(self, attrname):
            print('Trace:' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper


@Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)


@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    food = Spam()
    food.display()
    print([food.fetches])

    bob = Person('Bob', 40, 50)
    print(bob.name)
    print(bob.pay())

    print("===============")
    sue = Person('Sue', rate=100, hours=60)
    print(sue.name)
    print(sue.pay())

    print(bob.name)
    print(bob.pay())
    print([bob.fetches, sue.fetches])
