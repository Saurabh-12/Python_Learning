# Priority Queues using List
customers = []
customers.append((2, "Saurabh")) #no sort needed here because 1 item. 
customers.append((3, "Pheku"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((1, "Kumar"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((4, "Bhanu"))
customers.sort(reverse=True)
while customers:
     print(customers.pop(0))
#Will print names in the order: Bhanu, Pheku, Saurabh, Kumar. 
print("----------"*10)
# 2. Using heapq
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
     print(heapq.heappop(customers))
#Will print names in the order: Riya, Harry, Charles, Stacy.
print("----------"*10)
# 3. Using queue.PriorityQueue
from queue import PriorityQueue
#we initialise the PQ class instead of using a function to operate upon a list. 
customer1 = PriorityQueue() 
customer1.put((2, "Khesav"))
customer1.put((3, "Madhav"))
customer1.put((1, "Hari"))
customer1.put((4, "Riya"))
while customer1:
    print(customer1.get())
#Will print names in the order: Hari, Keshav, Madhav, Riya.