from tkinter import *
from random import shuffle

def main():
    f = open("demofile.txt", "r")
    stringText = f.read()

    questionObjectManager = QuestionObjectManager()
    questionComposite = processParseQuestionBank(stringText)

    # print("question Composite: "+str(questionComposite))
    questionObjectManager.setQuestionList(questionComposite)
    print("question Composite in QOM: " + str(questionObjectManager.getQuestionList()))


    # possibleAnswerList = questionObjectComposite[0].getAnswerListComposite()
    # firstQuestion = questionObjectComposite[0]
    # correctAnswersList = firstQuestion.getCorrectAnswer()
    # questionList = firstQuestion.getAnswerListComposite()
    # print(correctAnswersList)
    # print(questionList)

    #construct question, randomizing answers
    questionObjectManager.createTest(1)




















def parseIntoQuestionObjectsList():
    pass
def instantiateQuestion():
    pass
def randomizeQuestion():
    pass

def processParseQuestionBank(str_to_parse):
    data_set_group_0_1 = str_to_parse.split('QUESTION')

    # data_set_group_0_2 = []
    data_set_group_0_1.pop(0)
    questionObjectComposite = []
    intervalIndex = 0
    for val in data_set_group_0_1:
        # if(intervalIndex == 0):
        possibleAnswerIndex = 0
        questionContainer = val.splitlines()
        questionContainer = list(filter(None, questionContainer))
        questionNumber = questionContainer[0].replace(' ','')
        #create data object
        questionObj = QuestionObject()

        # print(questionContainer)

        questionObj.setQuestionNumber(questionNumber)
        questionObj.setProblem(questionContainer[1])
        questionPieceIndex = 0

        # Parse correct answer
        for questionPiece in questionContainer:
            if (questionPiece.find("Correct") == 0):
                questionObj.setCorrectAnswer(questionPiece)
            questionPieceIndex += 1

        questionObjectComposite.append(questionObj)

        # Parse answer list
        for val in questionContainer:
            if(possibleAnswerIndex > 1):
                # print(val)
                if(val.find("Correct") == 0):
                    isContinueCalculating = False
                    break
                questionObj.parseAnswer(val)
            possibleAnswerIndex += 1

        intervalIndex += 1

    return questionObjectComposite

def createDisplayList(questionList):
    displayContainer = []
    for question in questionList:
        displayObject = "Question "+question[0]

        #associateAnswer with bound correct answer object
        #Append new line questionList attributes
        displayContainer.append(displayObject)
    return displayContainer


class QuestionObject:
    def __init__(self):
        self.correctAnswer = 'Error: Check \'Correct\' answer format'
        self.answerListComposite = []
        self.randomizedList = []

    def setRandomizedList(self, randomizedList):
        self.randomizedList = randomizedList
    def getRandomizedList(self):
        return self.randomizedList
    def setQuestionNumber(self, questionNumber):
        self.questionNumber = questionNumber
    def getQuestionNumber(self):
        return self.questionNumber
    def setProblem(self, problem):
        self.problem = problem
    def getProblem(self):
        return self.problem
    def setCorrectAnswer(self, correctAnswer):
        self.correctAnswer = correctAnswer
    def getCorrectAnswer(self):
        return self.correctAnswer
    def parseAnswer(self, answerString):
        answerList = answerString.split(". ")
        self.answerListComposite.append(answerList)
    def getAnswerListComposite(self):
        return self.answerListComposite

    def getIsAnswered(self):
        return self.isAnswered
    def setIsAnswered(self, isAnswered):
        self.isAnswered = isAnswered
    # def isCorrectAnswerListSubmited(self, questionList, answerList):


class QuestionObjectManager:
    def __init__(self):
        self.ranomizedQuestionsList = []
        self.questionList = []

    #start on first question or randomize questions.
    #saving state of test completed
    #sampling or entirety
    #I want a 50 queston sample
    #I want to iterate through entire list

    def setQuestionList(self, questionList):
        self.questionList = questionList
    def getQuestionList(self):
        return self.questionList


    def createTest(self, caseType):
        if(0):
            # Support for sample sized test
            pass
        if (1):
            # print("questionList: "+str(self.getQuestionList()))
            # This is wrong it needs to be one individual question per.... Ah needs to randomize questions first.
            # Set randomized list at another time.
            # print("Question list1 " + str(self.getQuestionList()))
            self.shuffleQuestionList()

            testInstance = Test()

            print("Question list1 "+ str(self.getQuestionList()))
            testInstance.setQuestionList(self.getQuestionList())
            #
            print("Question list2 " + str(testInstance.getQuestionList()))
            testInstance.getQuestionList()


            testInstance.randomizeQuestionList()
            # testInstance.setCurrentQuestion()
            testInstance.startTest()



        if (2):
            # Support for loading test states from previous exams
            pass






            # print("shuffle: " + str(shuffledList))
                # print(question.getAnswerListComposite())
                # question.setRandomizedList(self.randomizeQuestionAnswers(question.getAnswerListComposite()))





            # self.setCurrentQuestion()

                # print(question.getRandomizedList())
                # print(question.getQuestionNumber())



    def shuffleQuestionList(self):
        list = self.getQuestionList()#[20, 16, 10, 5];
        shuffle(list)
        print("Reshuffled list : ", list)
        self.setQuestionList(list)

    def calculateQuestionSuccess(self):
        self.associateQuestionAnswersWithRandomizedResults()




    def associateQuestionAnswersWithRandomizedResults(self):
        # It knows the current question, randomized question list, answer list,
        # Need selected answer positioning.

        self.getRanomizedQuestionList()

        #associate placement?
        #Or... check if match, check if match
            # position selected equates to answer list,
               # check if answerList selected matches currently selected.
                # currently selected returned as a list.


    def setCurrentQuestion(self, questionObject):
        pass
    def randomizeQuestionList(self):
        shuffledList = shuffle(self.getRandomizedQuestionList())
        print("shuffle: " + str(shuffledList))
        return shuffledList

    def getRandomizedQuestionList(self):
        return self.randomizedQuestionsList
    def setRandomizedQuestionList(self, randomizedQuestionList):
        self.randomizedQuestionList = randomizedQuestionList

    def randomizeQuestionAnswers(self, answerList):
        shuffledList = shuffle(answerList)
        print("shuffle: "+ str(shuffledList))
        return shuffledList
    def getOriginalAnswerFormation(self):
        pass


    def setOriginalQuestionList(self, question):
        pass
    def getOriginalQuestionList(self):
        pass


class Test:
    def __init__(self):
        self.randomizedQuestionList = []
        self.questionList = []
        self.completedQuestions = []
        self.currentQuestionIndex = 0

    def randomizeQuestionList(self):
        self.randomizedQuestionList = shuffle(self.getQuestionList())

    def setQuestionList(self, questionList):
         self.questionList = questionList
    def getQuestionList(self):
        return self.questionList

    def changeToNextQuestion(self):
        # Handled elsewhere to give functionality to go back to previous questions without adding to completed list issues.
        self.handleCompletedQuestionChange()
        #Set current question isAnswered
        self.getCurrentQuestion().setIsAnswered(1)

        # self.setCurrentQuestion()
    def handleCompletedQuestionChange(self):
        # If currentQuestion has already been added,
        pass
        # for questionObject
        # currentQuestionIndex

    def setCurrentQuestion(self, currentQuestion):
        self.currentQuestion = currentQuestion
    def getCurrentQuestion(self):
        return self.currentQuestion



    def startTest(self):

        root = Tk()
        root.geometry('1400x800')

        questionlist = self.getQuestionList()#["A", "B", "C"]
        selectedAnswerList = []
        textAnswerList = []
        buttonList = []

        def ShowChoice():
            for selectedAnswer in selectedAnswerList:
                print(selectedAnswer.get())

        for counter, choiceText in enumerate(questionlist, 1):
            Label(root, text=choiceText).grid(row=counter, column=0)
            var = IntVar()
            for i in range(1, 2):
                textAnswerList.append([str(counter), choiceText])
                # print("I value created: "+str(i))
                button = Radiobutton(root, variable=var, value=i, command=ShowChoice)
                button.grid(row=counter, column=i)
                buttonList.append(button)
                selectedAnswerList.append(var)

        correctAnswersList = []  # correctAnswersList

        answerMatchingComposite = []

        def confirmAnswer():
            # create answerBooleanList to be appended later to textAnswerList
            answerBooleanList = []
            selectedAnswerIndex = 0
            for selectedAnswer in selectedAnswerList:
                # print("hit "+str(selectedAnswer))
                # for each selected answer, if case met return true, continue
                # else return false
                if (selectedAnswer.get() == 1):
                    # print("true at index: "+str(selectedAnswerIndex))
                    answerBooleanList.append("1")
                else:
                    answerBooleanList.append("0")
                selectedAnswerIndex += 1

            # append is selected
            appendTrueSelectedValueCount = 0
            for textAnswer in textAnswerList:
                if (len(textAnswer) == 3):
                    print("I'm at index 3")
                    del textAnswer[2:3]
                textAnswer.append(answerBooleanList[appendTrueSelectedValueCount])
                appendTrueSelectedValueCount += 1
            # print(selectedAnswerList)
            print(textAnswerList)
            print(str(len(textAnswerList)))

            # instantiate is matching list
            for textAnswer in textAnswerList:
                correctAnswerIndex = 0
                answerMatchingList = [textAnswer]
                answerMatchingComposite.append(answerMatchingList)
                selectedAnswerText = textAnswer[1]

                for correctAnswer in correctAnswerList:
                    if (selectedAnswerText == correctAnswer):
                        isAnswerMatching = True
                    else:
                        isAnswerMatching = False
                    answerMatchingList.append(isAnswerMatching)
            print(textAnswerList)
            print(answerMatchingComposite)

            # calculate are answers correct


            # filter isAnswerMatchingList, if isNotTrue found then tag answer as incorrect.
            # Case in which success? Case in which fail?
            # Given that all answers in correct answer list criteria need to be met, or wrong.
            # Also not too many answers given, or wrong answers selected.
            # Perhaps finding where criteria is not met, and if found then wrong.

            # iterate through corr
            # print(correctAnswer)

            selectedChoices = []
            for selectedAnswer in selectedAnswerList:
                # print(selectedAnswer.get())
                selectedChoices.append(selectedAnswer.get())
            print(selectedChoices)

            # selectedChoices = [0,0,0,0,1,1,0,0]
            answersList = [1, 1, 1, 0, 0, 0, 0, 0]

            # index = 0
            # while(index < len(selectedChoices)):
            #     if(selectedChoices[index] == answersList[index]):
            #         print("true")
            #     else:
            #         print("false")
            #     index += 1

        def deselectAnswers():
            for selectedAnswer in selectedAnswerList:
                selectedAnswer.set(0)

            print(textAnswerList)
            print(str(len(textAnswerList)))

        deselectOptionsButton = Button(text="Deselect Answers", command=deselectAnswers)
        deselectOptionsButton.place(x=70, y=200)

        confirmAnswerButton = Button(text="Confirm Answer", command=confirmAnswer)
        confirmAnswerButton.place(x=70, y=150)

        root.mainloop()

if __name__ == "__main__": main()
