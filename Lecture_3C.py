#Name: Soon Sam R. Santos
#Date: January 8, 2017
#Session: 6.189 Lecture 3 (Part C)
#Lecture_3C.py

#Function to test if the leter is a vowel
def is_a_vowel(b):
    #Testing if it is a vowel
    if b=='a' or b=='e' or b=='i' or b=='o' or b=='u':
        #Return True if b is a vowel
        return True
    elif b=='A' or b=='E' or b=='I' or b=='O' or b=='U':
        #Return True if b is a capital vowel
        return True
    else:
        #Return False if b is neither a vowel nor a capital vowel
        return False

##Testing
print is_a_vowel("a")
print is_a_vowel("I")
print is_a_vowel("B")

#Takes a phrase, and returns a string of all the vowels
#Defining the functions, the parameter is the phrase
def vowels_in_phrase(phrase):
    #Taking an empty string to store all the vowels
    allvowels=''
    #Passing through eache letter in the phrase
    for letter in phrase:
        #Using the other function to test whether the letter is a vowel or not 
            if is_a_vowel(letter):
                #Adding the vowel to the string
                allvowels=allvowels+letter
    #Return the string with all the vowels
    return allvowels
        
#Testing the functions
print "The vowels in the phrase Soon Sam are:", vowels_in_phrase("SoonSam")
print vowels_in_phrase("HellO, WOrld!")
print vowels_in_phrase("klxn")






                
