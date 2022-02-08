from threading import Thread, Lock
import time

l1 = Lock()
l2 = Lock()

def m1(name):
    print(f'Thread {name} about to lock l1')
    with l1:
        print(f'Thread {name} has lock l1')
        print(f'Thread {name} about to lock l2')
        with l2:
            print(f'Thread {name} run into deadlock.')


def m2(name):
    print(f'Thread {name} about to lock l2')
    with l2:
        print(f'Thread {name} has lock l2')
        print(f'Thread {name} about to lock l1')
        with l1:
            print(f'Thread {name} run into deadlock.')


t1 = Thread(target=m1, args=['m1'])
t2 = Thread(target=m2, args=['m2'])

t1.start()
t2.start()