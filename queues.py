"""
queues 
"""

queue = ["p1", "p2", "p3", "p4", "p5"]

#enequeue - enter

queue.append("p6")
print("the que is", queue)

#if it is given how many peope left the queue
m = int(input("Enter the number of people left the queue:: "))
print(queue[m:])