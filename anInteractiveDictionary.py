# Master Python through building real-world applications(Part 1)
# BUILDING AN INTERACTIVE DICTIONARY
'''
  Step 1-- The Data.
-Here we load data in .json format but will be stored in "data" variable as py 'dictionary'
Data is in JSON format (JavaScript Object Notation)
Is a minimal, readable(for both -humans &computers)format for structuring data.
It has a key &a value associated with the key.

  Step 2-- Check for non existing words
-Here we use basic if-else statement
If the word is not present in the data, we print "The word doesnt exist..."

  Step 3-- The case-sensitivity
-We convert the entered words all to lower case using.... lower() method.
use.... else-if codition.
-For words that start with capital letters (eg. Trevor, Kampala)
-For definition of acronyms (eg. USA, NATO)

  Step 4-- Closest match 
-This programm suggests you a correct word while you make a tying error in the search bar.
it is done with help of two functions:
 i).SequenceMatcher()
    -This gives a ratio of how two words are close!
    
  ii).get_close_mathes(word, posibilities, n=1, cutoff=0.75)
    -This gives the closest word(s) of all the possibilities!

    step 5--
'''
   # import library
import json
from difflib import get_close_matches

# load the json data as python dictionary
# Try tying "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("data.json"))

# Function for retriving defition
def retrive_definition(word):

    #Removing the case-sensitivity from the program
    #Convert all letters to lower-case coz our data is in that format
    word = word.lower()

    #Check for non existing words
    #1st elif: Make sure program returns definition of words starting with capital letters:
    #2nd elif: Make sure program returns deinition of shortfoams:
    #3rd elif: To find a similar word
     #--len > 0 because we can print only when the word has 1 or more close matches
     #--In the return statement, the last [0] represents the first element from the list of close matches 

    if word in data:
        return data[word]
    
    elif word.title() in data:   #1st
        return data[word.title()]

    elif word.upper() in data:   #2nd
        return data[data.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:   #3rd
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        
        #If the answer is yes, retrive definition of suggested word
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):  
            return("The word doesn't exit, try another word!") 
        else:
            return ("We don't understand your entry. use 'y' or 'n'!")

# Input from user
word_user = input("Enter a word: ")

# Retrive the definition using function and print the result
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-", item)

#For words having single definition
#Also we remove the square braces around the output
else:
    print("-", output)

print('\n    Thanks for using Interactive Dictionary! -- @TreVoR \n')

