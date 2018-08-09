# -*- coding: UTF-8 -*-

import random
from format import *
from opentdb import *
from vutils import *

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

def PrintBooleanQuestion(q):
    print("1: True 2: False")
    if (q["correct_answer"] == "True"): return 1
    else: return 2

def PrintQuestionProperties(q):
    print("Category: "+q["category"] +" Type: "+ types[str(q["type"])] +" Difficulty: "+ q["difficulty"])

def PrintQuestion(q):
    print("\n" + String_Formatting_Object.CreateFormattedString(q["question"]) + "\n")

def PrintQuestionChoicesAndReturnCorrectAnswer(q):
    if (q["type"] == "multiple"): ca = PrintMultipleChoicesRandomly(q["correct_answer"], q["incorrect_answers"])
    else: ca = PrintBooleanQuestion(q)
    return ca

def ValidateAnswer(q, ca, a):
    if a == ca:
        print("Correct!")
        return True
    else:
        print("Incorrect! Correct answer is '" + String_Formatting_Object.CreateFormattedString(q["correct_answer"]) + "'")
        return False

def AskQuestion(q):
    PrintQuestionProperties(q)
    PrintQuestion(q)
    ca = PrintQuestionChoicesAndReturnCorrectAnswer(q)
    a = int(input("Enter a number: "))
    return ValidateAnswer(q, ca, a)

def PromptChoice(dict, start="", si=1, end=""):
    for k, v in dict.items():
        start+= str(si) + ": " +str(v)+" "
        si+=1
    print(start)
    return int(raw_input(end))
