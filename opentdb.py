
from networking import *
import json

#trivia_db_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

class OpenTDB:

    difficulties = {0:"any", 1:"easy", 2:"medium", 3:"high"}

    categories = {9:"General Knowledge", 10:"Entertainment: Books", 11:"Entertainment: Film",
                    12:"Entertainment: Music", 13:"Entertainment: Musicals & Theatres", 14:"Entertainment: Television",
                    15:"Entertainment: Video Games", 16:"Entertainment: Board Games", 17:"Science & Nature",
                    18:"Science: Computers", 19:"Science: Mathematics", 20:"Mythology", 21:"Sports", 22:"Geogaphy",
                    23:"History", 24:"Politics", 25:"Art", 26:"Celebities", 27:"Animals", 28:"Vehicles",
                    29:"Entertainment: Comics", 30:"Science: Gadgets", 31:"Entertainment: Japanese Anime & Manga",
                    32:"Entertainment: Cartoon & Animations"}

    types = {"":"Any Type", "multiple":"Multiple Choice", "boolean":"True / False"}
    typen_n = {0:"Any Type", 1:"Multiple Choice", 2:"True / False"}
    type_n = {0:"", 1:"multiple", 2:"boolean"}

    @staticmethod
    def Types():
        return OpenTDB.types

    @staticmethod
    def GetTypes():
        return OpenTDB.typen_n

    @staticmethod
    def GetCategories():
        return OpenTDB.categories

    @staticmethod
    def GetDifficulties():
        return OpenTDB.difficulties

    def __init__(self, debug=False):
        self.debug = debug
        self.dict = False
        self.url = False
        self.low = 0
        self.high = False

    def __LoadPageAsDictionary(self):
        self.dict = json.loads(Web_Util.LoadPage(self.url))

    def __RequestResults(self):
        self.__LoadPageAsDictionary()
        if (self.dict["results"] == []):
            if self.debug:  print("Response Failed! Could not get a valid response.\n'"+self.url+"'")
            self.dict = False
        else: self.dict = self.dict["results"]

    def __InitURL(self, amnt):
        base_url = "https://opentdb.com/api.php?amount="+str(amnt)
        if (self.category <= 32 and self.category >= 9):
            base_url += "&category="+str(self.category)
        if (self.difficulty <= 3 and self.difficulty >= 1):
            base_url += "&difficulty="+str(self.difficulties[self.difficulty])
        if (self.type <= 2 and self.type >= 1):
            base_url += "&type="+str(self.type_n[self.type])
        self.url = base_url

    def __CreateURLAndGetRequest(self, amnt):
        self.__InitURL(amnt)
        self.__RequestResults()

    def __GetBestRequest(self):
        if self.high == False: self.high = self.amount
        med = int(self.low + (self.high-self.low)/2)
        if self.high == 0 or med == 0:
            self.dict = False
            return
        if self.high == self.low or self.low == med or self.high == med:
            self.__CreateURLAndGetRequest(self.low)
            return
        self.__CreateURLAndGetRequest(med)
        if self.dict == False: self.high = med
        else: self.low = med
        self.__GetBestRequest()

    def __ClearSort(self):
        self.high = False
        self.low = 0

    def __SetProperties(self, amount, category, difficulty, type):
        if amount > 50: amount = 50
        self.amount = amount
        self.category = category
        self.difficulty = difficulty
        self.type = type

    def GetRequest(self, amount, category, difficulty, type):
        self.__SetProperties(amount, category, difficulty, type)
        self.__GetBestRequest()
        self.__ClearSort()
        return self.dict

    def GetDifficulty(self):
        return self.difficulty

    def GetType(self):
        return self.type

    def GetCategory(self):
        return self.category
