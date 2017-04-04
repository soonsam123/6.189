#Name: Soon Sam
#Date: Dec 29, 2016
#Session: lecture 2
#lecture 2 - C.py
if 9>5:
    print "Yes, 9 is greater than 5"
if 9!=5:
    print "Yes, 9 is not equal to 5"
if 10>6:
    print "Yes 10 is greater than 6"
else:
    print "No"
if not 10>3 and 10<3:
    print "No"
#Traffic light example
light_color= raw_input("What color is the traffic light? ")
light_color=light_color.lower()
print light_color
if light_color== "red":
    print "You should stop"
elif light_color=="yellow":
    print "Slow down!"
elif light_color=="green":
    print "Go ahead!"
else:
    print "what country are you in??"
