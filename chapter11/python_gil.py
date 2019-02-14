import threading

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1


def sub():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=sub)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)
"""
-556312
"""
