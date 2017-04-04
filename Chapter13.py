#Name: Soon Sam R Santos
#Date: January 22, 2017
#Session: Lecture 6 - Chapter 13
#Chapter13.py

#*********************13*****************************
#***************Classes and Functions*****************

#*********************13.1*****************************
#************Time***************
#Defining a class called Time that records the time of the day
class Time:
    pass
#Create a new time (object) and asign attributes for hours, minutes and secods.
time=Time()
time.hours=11
time.minutes=59
time.seconds=60

#State diagram:
#time --> hours    --> 11
#         minutes  --> 59
#         seconds  --> 60

#Function to print the time
def printTime(time):
    print str(time.hours)+":"+str(time.minutes)+":"+str(time.seconds)
    #str() is necessary, otherwise I would not be able to use + and there would be
    #a space between the numbers and collons. 11 : 59 : 60.
#Test case
    #In this case, time is my object that I inputed in the argument.
    #Concienditally, they have the same name.
print printTime(time)
#11:59:60
#None (Because I used print)
#Check if t1 comes after t2. If yes, return True. If not, return False
def after(t1,t2): #t1 is the second, t2 is the first time.
    #11:59:56, 11:59:56. OR 11:30:25, 11:30:10
    #If the hours are the same
    if t1.hours==t2.hours:
        #If the minutes are the ssame
        if t1.minutes==t2.minutes:
            #if the seconds are the same
            if t1.seconds==t2.seconds:
                #They don't come one after the other
                return False
            #if the seconds of t1 is bigger, then it comes after t2.
            if t1.seconds>t2.seconds:
                return True #t1 follows t2.
            else:
                #It comes before t2
                return False
        #11:35:45, 11:39:45 OR 11:46:60, 11:56:45
    #If the hours are the same
        #if the minutes of t1 is bigger than t2. 
        if t1.minutes>t2.minutes:
            return True #t1 comes after t2
        else:
            #t1 comes before t2
            return False
        #For this case, it doesn't matter the seconds
    #If the hours of t1 is bigger than t2
    if t1.hours>t2.hours:
        #t1 comes after t2.
        return True
    else:
        #t1 comes before t2
        return False
    #For this case, it doesn't matter the minutes and seconds.
#Testcase
#Instantiate
time1=Time()
time1.hours=10
time1.minutes=45
time1.seconds=36
time2=Time()
time2.hours=10
time2.minutes=45
time2.seconds=11

print after(time1,time2) #True

#Instantiate
time3=Time()
time3.hours=10
time3.minutes=45
time3.seconds=36
time4=Time()
time4.hours=10
time4.minutes=48
time4.seconds=11

print after(time3,time4) #False

#Instantiate
time5=Time()
time5.hours=10
time5.minutes=45
time5.seconds=36
time6=Time()
time6.hours=9
time6.minutes=48
time6.seconds=11

print after(time5,time6) #True

print "-------------------------------------"#Organazing

#*********************13.2*****************************
#************Pure functions***************

#A rough version of addTime
#PURE FUNCTIONS: 1 - No side effects, as asking input to the user. 
#                2 - Don't modify any of the objects passe through it as arguments.
def addTime(t1,t2):
    sum=Time()
    sum.hours=t1.hours + t2.hours
    sum.minutes= t1.minutes + t2.minutes
    sum.seconds= t1.seconds + t2.seconds
    return sum

#We will create two Time objects. One that will be the current time and the second
#that is the amount of the time to prepare a bread
currentTime=Time()
currentTime.hours= 9
currentTime.minutes= 14
currentTime.seconds= 30
breadTime= Time()
breadTime.hours= 3
breadTime.minutes= 35
breadTime.seconds= 0
#The time it will be ready is the sum of both times
doneTime=addTime(currentTime,breadTime)
print printTime(doneTime)
#12:49:30
#None (Because of print)

#The function is not completely correct. If the minutes or the seconds is bigger than
#60, it will not work properly

def addTime(t1,t2):
    sum=Time()
    sum.hours=t1.hours + t2.hours
    sum.minutes= t1.minutes + t2.minutes
    sum.seconds= t1.seconds + t2.seconds
    #If the seconds of the sum is bigger than 60
    if sum.seconds>=60:
        #I take out 60 seconds 
        sum.seconds=sum.seconds - 60
        #and add one minute
        sum.minutes= sum.minutes + 1
    #If the minutes of the sum is bigger than 60
    if sum.minutes>=60:
        #I take out 60 minutes
        sum.minutes= sum.minutes - 60
        #and add 1 hours
        sum.hours= sum.hours + 1
    #Now I can return the sum
    return sum
#This is now correct, but we will make this code smaller after.

#Testcase
time10=Time()
time10.hours= 9
time10.minutes= 14
time10.seconds= 30
time20= Time()
time20.hours= 3
time20.minutes= 55
time20.seconds= 0
doneTime2=addTime(time10,time20)
print printTime(doneTime2)
#13:9:30

print "-------------------------------------"#Organazing

#*********************13.3*****************************
#************Modifiers***************

#MODIFIERS: Change some of the argument of the function
def increment(time, seconds):
    time.seconds= time.seconds + seconds
    if time.seconds>=60:
        time.seconds= time.seconds - 60
        time.minutes = time.minutes + 1
    if time.minutes>=60:
        time.minutes= time.minutes - 60
        time.hours= time.hours + 1
#If the seconds if much greater than 60
#While statement
def increment(time, seconds):
    time.seconds= time.seconds + seconds
    while time.seconds>=60:
        time.seconds= time.seconds - 60
        time.minutes = time.minutes + 1
    while time.minutes>=60:
        time.minutes= time.minutes - 60
        time.hours= time.hours + 1        
#Now it is correct, but it is not the most efficient solution

#Exercise: Rewrite this function in which it doesn't contain any loops.
def increment(time, seconds):
    #I'll divide the seonds by 60 and take the lower integer
    new_sec= int(seconds/60)
    #If it is 0, it is because seconds is lower than 60, so I just add it.
    if new_sec==0:
        time.seconds= time.seconds + seconds
        return printTime(time)
    #Else, it is greater than 60. 
    else:
        #I take the integer to add in minutes
        time.minutes= time.minutes + int(seconds/60)
        #and the remainder I will add to seconds
        time.seconds= time.seconds + (seconds%60)
        return printTime(time)
#Instantiate
TIME=Time()
TIME.hours= 8
TIME.minutes= 45
TIME.seconds= 1
print increment(TIME, 150)
#8:47:31
#This function is not fully correctly. I'll not work in that much time
#I'll spend more time in the exercises
print "-------------------------------------"#Organazing

#*********************13.4*****************************
#************Which is better?***************

#MODIFIERS and PURE FUNCTIONS
#1 - Anything that can be done with one can be done also with the another.
#2 - Pure functions are faster to develop and less error-prone.
#3 - Modifiers convenient at times.
#4 - Write pure function whenever you are able to do so.
#Just write modifiers it the is a compelling advantage
print "-------------------------------------"#Organazing

#*********************13.5*****************************
#*******Prototype development versus planning**********
#PROTOTYPE DEVELOPMENT: Write a rough version of the program and start debugging
#Although this approach can be effective, it can lead to code that is unnecessarily
#complicated
#Alternarively
#PLANNED DEVELOPMENT: High-level insight can make the problem easier.
#Time is a really three-digit number in base 60
#Seconds: ones columns
#Minutes: sixty columns
#Hours: thirty sixty hundreds columns
#We were doing addition in base 60 in addTime and increment
#We could turn the time into a single number
def convertToSeconds(t):
    minutes = t.hours*60 + t.minutes #total minutes
    seconds = minutes*60 + t.seconds #total in seconds
    return seconds
#Now from this integer to the time object
def makeTime(seconds): #Receiving the time all in seconds
    #Creating a time object
    time=Time()
    time.hours = seconds // 3600 #Receive just the integer
    time.minutes = (seconds%3600) // 60 #The integer of the remainder by 60
    time.seconds = seconds%60 #Because of divisibility
    return time
def addTime_easy(t1,t2):
    #Taking both times and adding just the second part
    seconds= convertToSeconds(t1) + convertToSeconds(t2)
    #Returning the result already passed to time
    return makeTime(seconds)
#This is much easir, I convert all the time to seconds and add, after I just make the time.
#instantiate
time1=Time()
time1.hours= 10
time1.minutes= 50
time1.seconds= 54
time2=Time()
time2.hours= 5
time2.minutes= 45
time2.seconds= 60
result = addTime(time1,time2)
print printTime(result)

#Doing the same thing for increment. Adding seconds to some time.
def increment_easy(time, seconds): #I receive the time, and the quantity of seconds.
    #The total time will be the time in seconds plus the seconds
    totaltime = convertToSeconds(time) + seconds
    #Then I need to show it in Time, so I use makeTime to convert seconds to time
    return makeTime(totaltime)
#instantiate
time123=Time()
time123.hours= 10
time123.minutes= 50
time123.seconds= 54

#total will receive a class point
total = increment_easy(time123, 1000)
#Then I need to use printTime to see the coordinates do total
#total.hours ....
print printTime(total)    
    
print "-------------------------------------"#Organazing

#*********************13.7*****************************
#*******Algorithms**********
#ALGORITHMS: General solution to a class of problems
#They don't require any intelligence to carry out
