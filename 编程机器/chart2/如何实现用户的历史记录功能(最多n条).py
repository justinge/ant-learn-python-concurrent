from collections import deque
import pickle

q = deque([], 5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

pickle.dump(q, open("../../a.txt", "wb"))
print(pickle.load(open("../../a.txt", "rb")))
