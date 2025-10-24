import os
import json
import sys
from time import sleep

class Outgoing:
        spend = 0
        category = "Other"
        description = "None given"
        date = "None given"

        def __init__(self, spend, category, description, date):
            self.spend = spend
            self.category

class Question:
        #What is the question?
        text = ""
        #Is it a required input
        isRequired = False
        ID = "defaultId"
        #constructor
        def __init__(self, text, isRequired, questionId):
            self.text = text
            self.isRequired = isRequired
            self.ID = questionId

def prettyPrint(words):
    for char in words:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

def clearCommandLine():
    os.system('cls')

def budgetSetup():
    prettyPrint("Hello, welcome to the budget setup. I will ask a few questions and you need to answer the best you can. Required questions will be marked with an asterisk '*', and if you wish not to answer a question, leave it blank. \n")
    
    #code from https://www.geeksforgeeks.org/python/create-a-file-if-not-exists-in-python/
    file_path = "./PersonalExpenseTracker/setup.txt"

    try:
        with open(file_path, 'x') as file:
            questions = [Question("What is your name?: ", True, "Q1"),Question("How much money do you get per month?: ", False, "Q2"),Question("How much do you want to spend on food per month?: ",False, "Q3"),Question("How much do you spend on accomidation per month on average?: ", False, "Q4"),Question("How much do you want to spend on going out/fun activities a month?: ", False, "Q5")]
            answers = []
            # Ask questions
            for question in questions:
                prettyPrint(question.text + "\n")
                answer = input()
                answers.append([question.ID,answer])
            
            file.write(json.dumps(answers))

    except FileExistsError:
        prettyPrint(" You already have a setup file.")
        #take input if yes/no
        validAnswer = False
        while validAnswer == False:
            prettyPrint(" Do you want to reset it? y/n: \n")
            userInp = input()
            # if yes, open the file, and clear it of all data.
            if userInp == "y" or userInp == "Y":
                os.remove(file_path)
                clearCommandLine()
                budgetSetup()
                break
             # if no, abort setup.
            elif userInp == "n" or userInp == "N":
                validAnswer = True
                break
            # if non-valid answer, loop again. 
            else:
                prettyPrint("Sorry, that was not a valid answer. Type either the letter y, or the letter n.")

def takeOutgoing():
    
    prettyPrint("How much was spent?: \n")
    spending = input()
    questions = [Question()]

budgetSetup()