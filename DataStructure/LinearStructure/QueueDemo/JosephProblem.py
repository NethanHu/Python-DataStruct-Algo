from DataStructure.LinearStructure.Queue import Queue


def joseph_order(namelist: list[str], num) -> str:
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(1, num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

name_list = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(joseph_order(name_list, 3))