from multiprocessing import Process, Queue
import random


data = [2, 4, 6, 8, 10, 12, 14, 16]


def square(idx, x, queue):
    res = x * x
    queue.put((idx, res))


def main():
    queue = Queue()
    processes = [Process(target=square, args=(idx, val, queue)) for idx, val in enumerate(data)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    return queue, processes


def get_queue(queue, processes):
    unsorted_list = ([queue.get() for _ in processes])
    sorted_list = [val[1] for val in sorted(unsorted_list)]
    print(sorted_list)
    return sorted_list


if __name__ == '__main__':
    our_queue, our_processes = main()
    res = get_queue(our_queue, our_processes)
    print(res[2])
