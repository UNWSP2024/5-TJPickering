#Programmer: Timothy Pickering
#Date: 2/17/25
#Title: Basic Math Quiz

import random

def mathQuiz():
    num1 = random.randint(1, 1000) #Generate 2 random numbers
    num2 = random.randint(1, 1000)
    print(f"  {num1}\n+ {num2}\n------") #Display the math problem
    userAnswer = int(input("Enter your answer: ")) #Get user input
    correctAnswer = num1 + num2 #Calculate the correct answer
    if userAnswer == correctAnswer: #Check if user is correct
        print("Correct!\nCongratulations!")
    else:
        print(f"Oops!\nThe correct answer is {correctAnswer}.")

mathQuiz() #Call the function to run the quiz
