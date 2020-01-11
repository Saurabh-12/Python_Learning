from collections import deque 
  
class Queue:
    def __init__(self, max_size = 10):
        self._queue = deque(maxlen = max_size)

 
    def is_empty(self):
        return self._queue == []
 
    def enqueue(self, data):
        self._queue.append(data)
 
    def dequeue(self):
        return self._queue.popleft()
queue = Queue(4)
queue.enqueue("Saurabh")
queue.enqueue("Kumar")
queue.enqueue("Sharma")
queue.enqueue("Blogs")

print(queue._queue)
print(queue.dequeue())


