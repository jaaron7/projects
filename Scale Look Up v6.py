# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:24:16 2019

@author: kraskjo
"""

# Simple program to lookup notes in a major or minor scale 

#dictionary to convert user input into integers, used for ScaleLookup function below
notes_to_numbers = {"A": 1, "Bb": 2, "B": 3, "C": 4, "Db": 5, "D": 6, "Eb": 7, "E": 8, "F": 9, "Gb": 10, "G": 11, "Ab": 12,}

#dictionary to convert integers back into scale notes strings 
numbers_to_notes = {1: "A", 2: "Bb", 3: "B", 4: "C", 5: "Db", 6: "D", 7: "Eb", 8: "E", 9: "F", 10: "Gb", 11: "G", 12: "Ab",}

notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

major_intervals = [2,4,5,7,9,11]
minor_intervals = [2,3,5,7,8,10]
    
def ScaleLookup(user_root, interval):
                      
    scale_lookup = [user_root]
    
    conversion = notes.index(user_root) + 1
    
    if interval == "Major":
       for i in major_intervals:
           i = i + 1
           if i + conversion > 12:
               scale_lookup.append(notes[(conversion + i) - 12])
           else:
               scale_lookup.append(notes[(conversion + i)] 
  
"""
    if interval == "Minor":
       for i in minor_intervals:
           i = i + 1
           if i + conversion > 12:
               scale_lookup.append(notes[(conversion + i) - 12])
           else:
               scale_lookup.append(notes[(conversion + i)]  
"""

"""          
   else: #interval == "Minor":
        for i in minor_intervals:
           if i + conversion > 12:
               scale_lookup.append(numbers_to_notes[(conversion + i) - 12])
           else:
               scale_lookup.append(numbers_to_notes[(conversion + i)])
"""  
           
    scale_string = str(scale_lookup).strip("[],")  
       
    print("Here are the notes in the key of " + user_root + " " + interval + ": " + scale_string)
    

"""
root = input("Enter root note: ")
if root in notes_to_numbers:
   interval = input("Enter major or minor")
   if interval not in ("major","minor"):
       
else:
    break
"""
"""
root = input("Enter root note: ")
while root not in notes_to_numbers:
    input("Please enter a valid root note:")
interval = input("Enter major or minor: ")
while interval not in ("major", "minor"):
    input("Please enter major or minor:" )
"""

#ScaleLookup(root, interval)

  
ScaleLookup((input("What's the root note? ")), input("Major or Minor? "))

#