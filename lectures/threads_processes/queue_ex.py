from multiprocessing import Process, Queue
import random


def rand_val(queue):
    num = random.randint(1, 50)
    print(num)
    queue.put(num)


def main():
    queue = Queue()
    processes = [Process(target=rand_val, args=(queue,)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    return queue, processes


def get_queue(queue, processes):
    print([queue.get() for _ in processes])


if __name__ == '__main__':
    our_queue, our_processes = main()
    get_queue(our_queue, our_processes)