#Name: Soon Sam R. Santos
#Date: January 10, 2017
#Session: 6.189 Lecture 4 (Part B)
#Lecture_4B.py

#How to create lists
new_list=[3,4,5,6]
print "new_list is:", new_list

#Slice them
print "From the first to the third element of the list:",new_list[0:3]
print "From the second to the last:",new_list[1:]
print "From the first to the fourth:",new_list[:4]
print "The whole list:",new_list[:]

#Travel throughout the elements
for item in new_list:
    print item
#Outputs each element without brackets
    
#Lists are mutable
new_list[2]=1000
print new_list

#append add a new element
new_list.append(87)
print new_list
#Or I can use insert too.
new_list.insert(0,86) #First: the position;  Second: The number
print new_list
#Delete an element using del or remove
del new_list[0]
print new_list

new_list.remove(1000) #The number I want to remove, not the position.
new_list.remove(87)
print new_list

print "-------------------------------------------------"
#PRACTICING
soon_list=[1,2,3,4,5,6,7,8,9,10]
del soon_list[0]
#Delete 1
soon_list.remove(2)
#Delete 2
soon_list.append(1)
#Add 1
soon_list.insert(0,2)
#Add 2 in the first position
print soon_list
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
