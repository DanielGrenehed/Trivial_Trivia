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
    
def AskQuestion(q):
    print("Category: "+q["category"] +" Type: "+ types[str(q["type"])] +" Difficulty: "+ q["difficulty"])
    print("\n"+CS(q["question"])+"\n")

    if (q["type"] == "multiple"): ca = PrintMultipleChoicesRandomly(q["correct_answer"], q["incorrect_answers"])
    else: 
        print("1: True 2: False")
        if (q["correct_answer"] == "True"): ca = 1
        else: ca = 2
    
    a= int(input("Enter a number: "))
    if a== ca:
        print("Correct!")
    else: 
        print("Incorrect! Correct answer is '"+CS(q["correct_answer"])+"'")
    return 

def PromptChoice(dict, start="", si=1, end=""):
    for k, v in dict.items():
        start+= str(si) + ": " +str(v)+" "
        si+=1
    print(start)
    return int(raw_input(end))

def FindBestValue(amnt, cat , df, tp, low=0, high=False):
    if high == False: high = amnt
    med = low + (high-low)/2
    if high == low or low == med or high == med: 
        rq = CreatGetRequest(low, cat, df, tp)
        return rq
    tst = CreatGetRequest(med, cat, df, tp)
    if tst == False: return FindBestValue(amnt, cat, df, tp, low, med)
    else: return FindBestValue(amnt, cat, df, tp, med, high)
    

def FindBestRequest(amnt, cat, df, tp):
    rq = CreatGetRequest(amnt, cat, df, tp)
    if rq == False:
        return FindBestValue(amnt, cat, df, tp)
    else : return rq

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
