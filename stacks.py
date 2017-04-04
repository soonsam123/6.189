# Name: Soon Sam R Santos
# Date: January 26, 2017
# Session: Homework 3
# stacks.py

#Stacks are the opposite of queue(FIFO), they use (LIFO)
#The last term to be added, will be the first to be removed. While in FIFO the last to be added is the last to be removed.
#Summarazing, in removing I must remove the last term of the list. Not the first.
#Use : __init__, push and pop
class Stack:
    def __init__(stack):
        #Method to initializate in and out with empty lists.
        stack.in_stack=[]
        stack.out_stack=[]
    def push(stack, term):
        #Method to add a term into stack.
        stack.in_stack.append(term)
    def pop(stack):
        #If the list is empty I must show it.
        if len(stack.in_stack)==0:
            return "The stack is empty"
        #Method to remove the newest term.
        i= len(stack.in_stack) - 1 #Quantity of terms in stack. (-1 because when using in list it will start at 0)
        stack.out_stack.append(stack.in_stack[i]) #Adding the element removed to my out stack.
        removed = stack.in_stack[i] #Storing the element removed to show latter.
        del stack.in_stack[i]  #Deleting the element from my in stack list.
        return removed  #Showing the element that was removed.
stack=Stack()
print stack.push(5)
print stack.push(6)
print stack.pop()
#Should output 6
print stack.push(7)
print stack.pop()
#Should output 7
print stack.pop()
#Should output 5
print stack.pop()
#Should output "The stack is empty"

#Note: None will appear in my shell because I am priting and not doing it directly on the IDLE.
