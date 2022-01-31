import threading
import math


def quadratic_calculator(a, b, c):
    dis = (b ** 2) - (4 * a * c)

    if dis > 0:
        root1 = (-b - math.sqrt(dis)) / (2 * a)
        root2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f'Result: {root1} and {root2}')
    elif dis == 0:
        root1 = root2 = -b / (2 * a)
        print(f'Result: {root1} and {root2}')
    elif dis < 0:
        print('The quadratic equation has no real roots')


thread1 = threading.Thread(target=quadratic_calculator(6, 11, -35))
thread2 = threading.Thread(target=quadratic_calculator(5, -2, -9))

thread1.start()
thread2.start()
