import threading
import time


def function1():
    for i in range(5):
        print("Function 1: %s" % time.ctime(time.time()))
        time.sleep(1)


def function2():
    for i in range(5):
        print("Function 2: %s" % time.ctime(time.time()))
        time.sleep(2)


# 创建新线程
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

# 开启新线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("Exiting Main Thread")
