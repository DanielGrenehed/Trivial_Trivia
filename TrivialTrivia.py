# -*- coding: UTF-8 -*-

from game import *

def PromptChoice(dict, start="", si=1, end=""):
    for k, v in dict.items():
        start+= str(si) + ": " +str(v)+" "
        si+=1
    print(start)
    return int(raw_input(end))


def Setup():
    amnt = int(input("How many questions?(max 50) "))
    cat = PromptChoice(OpenTDB.GetCategories() , "1: Any ", 2, "Choose catgory: ") + 7
    tp = PromptChoice(OpenTDB.GetTypes(), "", 1, "Choose type: ") - 1
    df = PromptChoice(OpenTDB.GetDifficulties(), "", 1, "Choose difficulty: ") - 1
    db = OpenTDB()
    page_dict = db.GetRequest(amnt, cat, df, tp)
    if page_dict == False:
        print("Could not find any questions of that type!")
        return
    print("\nFound "+str(len(page_dict))+" questions!")

    game = Trivia(page_dict)

    score = 0
    i = 1
    while not game.IsDone():
        print("\n\nQuestion "+str(i)+"!")
        if game.NextQuestion() : score += 1
        raw_input("press Enter to continue!")
        i+=1
    print("Score: "+str(score)+"/"+str(i-1))
    return

Setup()
