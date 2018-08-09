# -*- coding: UTF-8 -*-

from game import *

def Setup():
    amnt = int(input("How many questions?(max 50) "))
    cat = PromptChoice(categories , "1: Any ", 2, "Choose catgory: ")+7
    tp= PromptChoice(typen_n, "", 1, "Choose type: ")-1
    df = PromptChoice(difficulties, "", 1, "Choose difficulty: ") -1
    page_dict = FindBestRequest(amnt, cat, df, tp)
    if page_dict == False:
        print("Could not find any questions of that type!")
        return
    print("\nFound "+str(len(page_dict))+" questions!")

    i = 1
    for q in page_dict:
        print("\n\nQuestion "+str(i)+"!")
        AskQuestion(q)
        raw_input("press Enter to continue!")
        i+=1
    return

Setup()
