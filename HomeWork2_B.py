a_list=[3,5,6,12]
for num in a_list:
    print num
print "-----------------------------------------"
new_list=[0,0,0,0]
i=1
while i<=len(a_list):
    new_list[i-1]=a_list[-i]
    i+=1
print new_list
print "-----------------------------------------"
print [3*num for num in a_list]
print "-----------------------------------------"
newlist=['','','','']
i=0
while i<len(a_list):
    if a_list[i]<6:
        newlist[i]=False
    else:
        newlist[i]=True
    i+=1    
print newlist
