#Name: Soon Sam R Santos
#Date: January 5, 2016


#****************LECTURE 3***********************
#****************HOMEWORK 2***********************
#****************WEDNESDAY***********************

# ***************Section 6.9*********************
#****************MORE GENERALIZATION***********************

#Now I choose them number I will use in the table and I also choose
#the length of the line, whether it will apear 7 numbers in a line
#or just 1 number in a line.
def printMultiples(n, length):
    i=1
    while i<=length:
        print n*i, "\t",
        i+=1
    print
#For the Table I change nothing, just when I print the Multiples I use
#i to be them number, that will start in 1 and finish in high(the high
#of the table) and I print the length of the printMultiples as the high,
#by this way, thei high will be equal the length. Even Table.
#def printMultTable(high):
 #   i=1                   #Here each number was appearing twice.
  #  while i<=high:
   #     printMultiples(i,high) 
    #    i=i+1  #It was no working with i+=1(IDK)

#Now I don't want to repeat numbers. If I print 1*1,1*2,1*3,1*4
#(1*2,1*3 and 1*4) will repeat when I multiply (2*1,3*1,4*1)
#Therefore I will multiply each number just until his value
#1*1 (Finish), 2*1, 2*2 (Finish), 3*1,3*2,3*3 (Finish)
def printMultTable(high):
    i=1
    while i<=high:
        printMultiples(i,i) #To provide that I use i,i 
        i=i+1  #It was no working with i+=1(IDK)
