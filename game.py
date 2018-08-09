# -*- coding: UTF-8 -*-

import random
from format import *
from opentdb import *

if sys.version_info[0] == 3:
    def raw_input(x): # define raw_input for python3
        return input(x)

def PrintMultipleChoicesRandomly(ct, it):
    cc = it
    cc.append(ct)
    random.shuffle(cc)
    cs = ""
    i=1
    for c in cc:
        cs += str(i) + ": " + String_Formatting_Object.CreateFormattedString(c) + " "
        i+=1
    print(cs)
    return (cc.index(ct)+1)

#ask question and return result
def AskQuestion(q):
    # print question and properties
    print("Category: "+q["category"] +" Type: "+ types[str(q["type"])] +" Difficulty: "+ q["difficulty"])
    print("\n" + String_Formatting_Object.CreateFormattedString(q["question"]) + "\n")

    #print choices
    if (q["type"] == "multiple"):
        # multiple answer question
        ca = PrintMultipleChoicesRandomly(q["correct_answer"], q["incorrect_answers"])
    else:
        # boolean question
        print("1: True 2: False")
        if (q["correct_answer"] == "True"): ca = 1
        else: ca = 2

    #prompt user for answer
    a = int(input("Enter a number: "))
    #validate answer
    if a == ca:
        print("Correct!")
        return True
    else:
        print("Incorrect! Correct answer is '" + String_Formatting_Object.CreateFormattedString(q["correct_answer"]) + "'")
        return False

def PromptChoice(dict, start="", si=1, end=""):
    for k, v in dict.items():
        start+= str(si) + ": " +str(v)+" "
        si+=1
    print(start)
    return int(raw_input(end))
