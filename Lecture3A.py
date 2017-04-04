#Name: Soon Sam R. Santos
#Date: January 7, 2017
#Session: Lecture 3 (Part A)
#Lecture3A.py


base=10
exp=4
#Here I can see that eventough I gave a value to the base outside and inside def
#each value will not influence in the other, therefore the value inside def
#will always the same and outside too.
def helloworld():
    base=20
    print "inside of helloworld base is", base
    print "Hello, World!"
    return 15 #When I return, the value appear on the screen

#This actually print the value returned and not 20
print helloworld()

#It's still the value of the base outside = 20
print "outside of helloworld base is", base

print "-----------------------------------------------------------"

#The output is 5 and None because it is not returning any value
def ret_5():
    print 5
print ret_5()

print "-----------------------------------------------------------"

#Return will show the result of the mathematic equation I wantq
#Return is a way to show a value and break the loop imediatelly
def compute_exp(base, exp):
    print 'inside of function base is', base
    print 'inside of function exp is', exp
    return base**exp
#the value outside of function keep being the same base=10 exp=4   
print "outside of function, base is", base
print "outside of function, exp is", exp
print compute_exp(5,0)
print compute_exp(5,3)
print compute_exp(8,2)
