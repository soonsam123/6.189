#Exercise 1.14 Confirming Answers
num=10
while num>3:
    print num
    num -= 1
print ("--------------")
divisor=2
for i in range (0,10,2):
    print i/divisor
print ("--------------")
num=10
while True:
    if num<7:
        break
    print num
    num-=1
print ("--------------")
count=0
for letter in 'Snow!':
    print "Letter #",count,"is",letter
    count +=1
print ("--------------")
i=10
while i>2:
    print i
    if i%2==0:
        i=i/2
    if i%2!=0:
        i+=1
    if i==2:
        print i
        break
