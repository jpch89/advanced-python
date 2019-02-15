import time
import threading

# 1. 通过 Thread 类实例化
"""
def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    print('get detail url started')
    time.sleep(4)
    print('get detail url end')


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=('', ))
    thread2 = threading.Thread(target=get_detail_url, args=('', ))
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    print('time elapsed: {}'.format(time.time() - start_time))

"""

"""
get detail html started
get detail url started
time elapsed: 0.0
get detail html end
"""

# 2. 通过继承 Thread 类来实现多线程
# 重写 run 方法
class GetDetailHTML(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):  # 这里放的就是 target 指向的东西
        print('get detail url started')
        time.sleep(2)
        print('get detail url end')

class GetDetailURL(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):  # 这里放的就是 target 指向的东西
        print('get detail url started')
        time.sleep(4)
        print('get detail url end')

if __name__ == '__main__':
    thread1 = GetDetailHTML('get_detail_html')
    thread2 = GetDetailURL('get_detail_url')
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('time elapsed: {}'.format(time.time() - start_time))
"""
get detail url started
get detail url started
get detail url end
get detail url end
time elapsed: 4.001728534698486
"""
