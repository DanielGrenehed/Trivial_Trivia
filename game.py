# -*- coding: UTF-8 -*-

import random
from format import *
from opentdb import *
from vutils import *

class Trivia:

    def __init__(self, questions):
        self.qdict = questions
        self.current_question = False
        self.current_question_number = 0
        self.done = False
        self.num_questions = len(questions)

    def __InitCurrentQuestion(self):
        self.current_question = self.qdict[self.current_question_number]

    def __ClearCurrentQuestion(self):
        self.right_answer = None
        self.current_question = None

    def __PrintQuestion(self):
        print("\n" + String_Formatting_Object.CreateFormattedString(self.current_question["question"]) + "\n")

    def __PrintQuestionProperties(self):
        print("Category: "+self.current_question["category"] +" Type: "+ types[str(self.current_question["type"])] +" Difficulty: "+ self.current_question["difficulty"])

    def __PrintBooleanChoices(self):
        print("1: True 2: False")
        if (self.current_question["correct_answer"] == "True"): self.right_answer = 1
        else: self.right_answer = 2

    def __PrintMultipleChoicesRandomly(self):
        Choices = self.current_question["incorrect_answers"]
        Choices.append(self.current_question["correct_answer"])
        random.shuffle(Choices)
        cs = ""
        i=1
        for c in Choices:
            cs += str(i) + ": " + String_Formatting_Object.CreateFormattedString(c) + " "
            i+=1
        print(cs)
        self.right_answer = (Choices.index(self.current_question["correct_answer"])+1)

    def __PrintQuestionChoices(self):
        if self.current_question["type"] == "multiple" : self.__PrintMultipleChoicesRandomly()
        else: self.__PrintBooleanChoices()

    def __ValidateAnswer(self, answer):
        if answer == self.right_answer:
            print("Correct!")
            return True
        else:
            print("Incorrect! Correct answer is '" + String_Formatting_Object.CreateFormattedString(self.current_question["correct_answer"]) + "'")
            return False

    def __PrintCurrentQuestion(self):
        self.__PrintQuestionProperties()
        self.__PrintQuestion()
        self.__PrintQuestionChoices()

    def __PromptAndValidateAnswer(self):
        answer = int(raw_input("Enter a number: "))
        result = self.__ValidateAnswer(answer)
        self.__ClearCurrentQuestion()
        return result

    def __AskQuestion(self):
        self.__InitCurrentQuestion()
        self.__PrintCurrentQuestion()
        return self.__PromptAndValidateAnswer()

    def NextQuestion(self):
        if self.done: return None
        result = self.__AskQuestion()
        self.current_question_number += 1
        return result

    def IsDone(self):
        if self.done: return True
        if self.current_question_number >= self.num_questions:
            self.done = True
            return True
        return False

    def AskQuestion(self, number):
        if number < 0 or number >= self.num_questions: return None
        self.current_question = self.qdict[number]
        self.__PrintCurrentQuestion()
        return self.__PromptAndValidateAnswer()
