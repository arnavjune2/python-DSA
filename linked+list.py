#creating a single linked list
from tkinter.messagebox import NO


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head= None):
        self.head = head

    #Linked list transversal
    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


    # Function to insert a new node at the beginning
    def push(self, new_node):
        if self.head:
            
            new_node.next = self.head
            self.head = new_node

    # Function to insert a new node at the end
    def append(self, new_node):
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    #Function to generate a linkedList from a array
    def generate(self, arr):
        curr = self.head
        for i in range(len(arr)):
            #print(1)
            if curr == None:
                #print(2)
                self.head = Node(arr[i])
                curr = self.head
            else:    
                #print(3)
                curr.next = Node(arr[i])
                curr = curr.next

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