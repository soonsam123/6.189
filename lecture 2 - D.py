#Name: Soon Sam
#Date: Dec 29, 2016
#Session: lecture 2
#lecture 2 - D.py
#Loop Examples
                   #************Number1***********#
name=raw_input("What is your name? ")
space=input("How many spaces did you type?")
letter_count=0 #Initializa the variable to count the letters
for letter in name: #colon
    print "Letter number", letter_count+1,"is", letter
    #Add '+1' in letter_count to not show 0 in the first term and
    #organize the sequence
    letter_count=letter_count+1
#get out of the loop to show this last line just once
print "There were", letter_count - space, "letters in the string", name    
                   



