import threading


def get_threads_count():
    return threading.active_count()


def crying_for(name):
    print(f"Im crying for {name}")


t1 = threading.Thread(target=crying_for, args=['video games'])
t2 = threading.Thread(target=crying_for, args=['summer'])

crying_for('free time')
print(f'Threads count before start: {get_threads_count()}')

t1.start()
t2.start()

print(f'Threads count before join: {get_threads_count()}')

t1.join()
t2.join()

print(f'Threads count: {get_threads_count()}')