
from networking import *
import json



#trivia_db_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"


difficulties = {0:"any", 1:"easy", 2:"medium", 3:"high"}
categories = {9:"General Knowledge", 10:"Entertainment: Books", 11:"Entertainment: Film", 12:"Entertainment: Music", 13:"Entertainment: Musicals & Theatres", 14:"Entertainment: Television", 15:"Entertainment: Video Games", 16:"Entertainment: Board Games", 17:"Science & Nature", 18:"Science: Computers", 19:"Science: Mathematics", 20:"Mythology", 21:"Sports", 22:"Geogaphy", 23:"History", 24:"Politics", 25:"Art", 26:"Celebities", 27:"Animals", 28:"Vehicles", 29:"Entertainment: Comics", 30:"Science: Gadgets", 31:"Entertainment: Japanese Anime & Manga", 32:"Entertainment: Cartoon & Animations"}
types = {"":"Any Type", "multiple":"Multiple Choice", "boolean":"True / False"}
typen_n = {0:"Any Type", 1:"Multiple Choice", 2:"True / False"}
type_n = {0:"", 1:"multiple", 2:"boolean"}

def CreateURL(an, cg, df, tp):
    base_url = "https://opentdb.com/api.php?amount="+str(an)
    if (cg <= 32 and cg >= 9): base_url += "&category="+str(cg)
    if (df <= 3 and df >= 1): base_url += "&difficulty="+str(difficulties[df])
    if (tp <= 2 and tp >= 1): base_url += "&type="+str(type_n[tp])
    return base_url

#loads page and converts to dictionary
def GetPageAsDictionary(url):
    page = Web_Util.LoadPage(url)
    return json.loads(page)

#Loads and validates page for results and returns a dictionary of questions
def GetRequestResults(url, print_error=False):
    page_dict = GetPageAsDictionary(url)
    if (page_dict["results"] == []):
        if print_error: print("Response Failed! Could not get a valid response.\n'"+url+"'")
        return False
    return page_dict["results"]

#Creates url and loads page as dictionary
def CreateGetRequest(amnt, cat, df, tp):
    return GetRequestResults(CreateURL(amnt, cat, df, tp))

#find request with most questions
def FindBestValue(amnt, cat , df, tp, low=0, high=False):
    if high == False: high = amnt #set highest result
    med = low + (high-low)/2
    if high == low or low == med or high == med: # return if best request found
        return CreateGetRequest(low, cat, df, tp)
    tst = CreateGetRequest(med, cat, df, tp) # get median request
    if tst == False: return FindBestValue(amnt, cat, df, tp, low, med)# median too high, set median as high
    else: return FindBestValue(amnt, cat, df, tp, med, high)# median was good, set as lowest

#test request and return best result
def FindBestRequest(amnt, cat, df, tp):
    if amnt > 50: amnt = 50
    rq = CreateGetRequest(amnt, cat, df, tp)
    if rq == False: #Original request failed
        return FindBestValue(amnt-1, cat, df, tp)
    else : return rq
