from threading import Thread


aLi = [0]
def func1(aLi):
    for i in range(100000):
        aLi[0] += 1

def func2(aLi):
    for i in range(100000):
        aLi[0] -= 1

t1 = Thread(target=func1, args=(aLi, ))
t2 = Thread(target=func2, args=(aLi, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(aLi)
