from threading import Lock

total = 0
# 声明一个锁
lock = Lock()


def add():
    global total, lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def sub():
    global total, lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


from threading import Thread
t1 = Thread(target=add)
t2 = Thread(target=sub)
t1.start()
t2.start()
t1.join()
t2.join()
print(total)

