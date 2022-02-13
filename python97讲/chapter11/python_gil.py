# gil global interpreter lock (cpython)
# python 中一个线程对应c语言中的一个线程
# gil使得同一时刻只有一个线程在一个cpu上执行字节码,无法将多个线程映射到多个cpu上执行
# gil会根据执行的字节码行数以及时间片释放gil. gil在遇到io的操作时主动释放
# import dis
#
#
# def add(a=4):
#     a = a + 1
#     return a
#
#
# print(dis.dis(add))
total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1



import threading

threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)
threading1.start()
threading2.start()
threading1.join()
threading2.join()
print(total)
