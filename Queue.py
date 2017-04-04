# Name: Soon Sam R Santos
# Date: January 25, 2017
# Session: Homework 3
# Queue.py
class Queue:
    #Method to initializate
    def __init__(queue):
        #My queue will begin with two empty lists, one for whom is in the queue
        #and other for whom is out.
        queue.in_stack=[]
        queue.out_stack=[]
        #Insert one element to queue.
    def insert(queue, element):
        #My in stack will store the element
        #By using append. I can't do it by queue.in_stack[0] = element
        queue.in_stack.append(element)
        #Remove one element from queue.
    def remove(queue):
        if len(queue.in_stack)==0:
            #If there is no element in the queue. I must show the message
            return "The queue is empty"
        else:
            #Else I remove the element that is more time in the queue
            queue.out_stack.append(queue.in_stack[0])
            removed= queue.in_stack[0]
            del queue.in_stack[0]
            return removed
queue=Queue()
queue.insert(5)
queue.insert(6)
queue.remove() #Outputs 5
queue.insert(7)
queue.remove() #Outputs 6
queue.remove() #Outputs 7
queue.remove() #Outputs the message: The queue is empty
