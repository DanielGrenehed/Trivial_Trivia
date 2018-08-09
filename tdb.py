# -*- coding: UTF-8 -*-

import random
from format import *
from request import *

def PrintMultipleChoicesRandomly(ct, it):
    cc = it
    cc.append(ct)
    random.shuffle(cc)
    cs = ""
    i=1
    for c in cc:
        cs += str(i)+": "+ CS(c) +" "
        i+=1
    print(cs)
    return (cc.index(ct)+1)

#ask question and return result
def AskQuestion(q):
    # print question and properties
    print("Category: "+q["category"] +" Type: "+ types[str(q["type"])] +" Difficulty: "+ q["difficulty"])
    print("\n"+CS(q["question"])+"\n")

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
        print("Incorrect! Correct answer is '"+CS(q["correct_answer"])+"'")
        return False

def PromptChoice(dict, start="", si=1, end=""):
    for k, v in dict.items():
        start+= str(si) + ": " +str(v)+" "
        si+=1
    print(start)
    return int(raw_input(end))

def Setup():
    amnt = int(input("How many questions?(max 50) "))
    cat = PromptChoice(categories , "1: Any ", 2, "Choose catgory: ")+7
    tp= PromptChoice(typen_n, "", 1, "Choose type: ")-1
    df = PromptChoice(difficulties, "", 1, "Choose difficulty: ") -1
    page_dict = FindBestRequest(amnt, cat, df, tp)
    print("\nFound "+str(len(page_dict))+" questions!")

    i = 1
    for q in page_dict:
        print("\n\nQuestion "+str(i)+"!")
        AskQuestion(q)
        raw_input("press Enter to continue!")
        i+=1
    return
