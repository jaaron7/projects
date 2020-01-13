# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:24:16 2019

@author: kraskjo
"""


scale_list = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
notes_to_numbers = {
        "A": 1,
        "Bb": 2,
        "B": 3,
        "C": 4,
        "Db": 5,
        "D": 6,
        "Eb": 7,
        "E": 8,
        "F": 9,
        "Gb": 10,
        "G": 11,
        "Ab": 12,
        }

numbers_to_notes = {1: "A", 2: "Bb", 3: "B", 4: "C", 5: "Db", 6: "D", 7: "Eb", 8: "E", 9: "F", 10: "Gb", 11: "G", 12: "Ab",}

"""def scale_lookup(root):
    root = notes_to_numbers[user_key]
    note2 = numbers_to_notes[root + 2]
    note3 = root + 4
    note4 = root + 5
    note5 = root + 7
    note6 = root + 9 
    note7 = root + 11
"""

#user_root = input("Key?") # ask user for note

def ScaleLookup(user_root):
    
    conversion = notes_to_numbers[user_root]
    
    note2 = conversion + 2
    if note2 > 12:
        note2 = numbers_to_notes[(conversion + 2) - 12]
    else:
        note2 = numbers_to_notes[conversion + 2]
        
    note3 = conversion + 4
    if note3 > 12:
        note3 = numbers_to_notes[(conversion + 4) - 12]
    else:
        note3 = numbers_to_notes[conversion + 4]  
        
    note4 = conversion + 5
    if note4 > 12:
        note4 = numbers_to_notes[(conversion + 5) - 12]
    else:
        note4 = numbers_to_notes[conversion + 5]
        
    note5 = conversion + 7
    if note5 > 12:
        note5 = numbers_to_notes[(conversion + 7) - 12]
    else:
        note5 = numbers_to_notes[conversion + 7]
        
    note6 = conversion + 9
    if note6 > 12:
        note6 = numbers_to_notes[(conversion + 9) - 12]
    else:
       note6 = numbers_to_notes[conversion + 9] 
        
    note7 = conversion + 11
    if note7 > 12: 
        note7 = numbers_to_notes[(conversion + 11) - 12]
    else:
       note7 = numbers_to_notes[conversion + 11] 
           
    print("Here are the notes for the key of " + user_root + ": " + user_root + note2 + note3  + note4 + note5 + note6 + note7)

ScaleLookup((input("In what key are you playing? ")))

#