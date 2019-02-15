import threading
from threading import Condition


class XiaoAi(threading.Thread):
    def __init__(self, lock):
        super().__init__(name='小爱')
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print('{}:在'.format(self.name))
        self.lock.release()



class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{}:小爱同学'.format(self.name))
            self.lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    tianmao = TianMao(lock)
    xiaoai = XiaoAi(lock)
    tianmao.start()
    xiaoai.start()
