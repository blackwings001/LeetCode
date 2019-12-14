from queue import Queue

q = Queue()
q.put(1)
print(q.qsize())
e = q.get()
print(q.qsize())