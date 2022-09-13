# first in first out
# [1,2,3,4]

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
queue.popleft()
if not queue:
    print("Empty")

# queue_var = ([])
# queue_var.append(1)
# queue_var.append(10)
# queue_var.append(100)
# queue_var.append(1000)
# queue_var.remove(1)
# print(queue_var)
