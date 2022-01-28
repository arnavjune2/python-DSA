#creating a single linked list
from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head= None):
        self.head = head

    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

#just initaiting a singly linked list    
if __name__=="__main__":
    my_LL = LinkedList()
    first_node = Node(56)
    second_node = Node(12)
    third_node = Node(90)

    my_LL.head = first_node
    my_LL.head.next = second_node
    second_node.next = third_node

    my_LL.print_list()