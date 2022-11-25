'''Project 9:
You have to build a dictionary (Or any other container of your choice) which contains multiple True/false type quiz questions.
Every participant/user will attempt 5 rounds and in each round random quiz questions will be displayed to the user/participant.
If the participant answers the quiz question correct, then congratulate him and add the scores.
At the end display the details and score of the participant.
(Student is free to decide the input and output layout for this mini project)
'''

print(" ***  *   * ***** *******    ******   ***  *     * *****")
print("*   * *   *   *        *     *       *   * **   ** *")
print("*   * *   *   *       *      *       *   * * * * * *")
print("*   * *   *   *      *       *   *** ***** *  *  * *****")
print("*   * *   *   *     *        *    *  *   * *     * *")
print("**  * *   *   *    *         *    *  *   * *     * *")
print(" ***   ***  ***** *******    ******  *   * *     * *****")
print("   *")
print("")

name=input("Enter your name:  ")
print("Hello,",name,"WELCOME TO MY PYTHON TRUE/FALSE TYPE QUIZ GAME !\n")

playing = input("Do you want to play ? (YES/NO) \n")
playing=playing.upper()
if playing != "YES":
    quit()
print("\nLets start!")

q1="RAM is a non-volatile memory (True/False)"
q2="Variables defined in a function are local to that function, unless bound by the global keyword (True/False)"
q3="There is usually only one correct solution to a problem involving decision structures (True/False)"
q4="The condition x <= y <= z is allowed in Python (True/False)"
q5="A Python while can implement a definite loop (True/False)"
q6="a and (b or c) == (a and b) or (a and c) (True/False)"
q7="An int can be converted to a string while a string cannot be converted to an int (True/False)"
q8="The if statement can only accept a Boolean expression as a condition (True/False)"

question={q1:"FALSE",q2:"TRUE",q3:"FALSE",q4:"TRUE",q5:"TRUE",q6:"TRUE",q7:"FALSE",q8:"TRUE"}

Score=0

import random
questionlist=[]
while(len(questionlist)!=5): # list of 5 questions
    i=random.choice(list(question.keys())) #Choose Random question from question pool and make a list of it
    if(i not in questionlist):
        questionlist.append(i) # make a list of random qustions

for i in questionlist:
    print("\n",i)
    ans=input("Enter the answer (TRUE/FALSE):  ")
    ans=ans.upper()
    if ans==question[i]:
        print("Congratulation ! your answe is correct you got 1 point")
        Score = Score + 1
        print("Your current score is :",Score)
    else:
        print("Your answer is wrong")
        print("Your current score is :",Score)
print("\nFinal score is :",Score)
print("\nYour",Score,"questions are correct !")
print("Your",5-Score,"questions are incorrect !")
print("\nyou got",(Score/5)*100,"%")