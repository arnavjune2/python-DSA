"""
stack follows:::: LIFO(i.e last in first out)
push, pop, peek
"""
stack = ['b 1', 'b 2', 'b 3', 'b 4', 'b 5']

# restriction is: I cannot have more then 5 books on the stack

stack.append("b 6")

if(len(stack)>5):
    print("stack overflow")

    #getting the top most book number from the stack
    last_book_number = int(stack[-1].split(" ")[-1]) #stack[-1](peek operation)
    print(f"last book number is {last_book_number}")
else:
    print("its ok")

#using pop
print(f"the topmost book is {stack.pop()}")
print(f"arr after using pop {stack}")



