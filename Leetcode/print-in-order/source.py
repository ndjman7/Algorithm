from queue import Queue


class Foo(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.q1.put(1)


    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.q1.get()
        printSecond()
        self.q2.put(2)


    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.q2.get()
        printThird()
