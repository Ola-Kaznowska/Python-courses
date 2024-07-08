import math

print("Welcome to Python Go IT.us!")

print()


for letter in ["1: Python Basic", "2: Python intermediate", "3: Python + AI", "4: Start IT"]:
    print(letter)


print()

user = input("Choose a programming course: ")




userSelection = input("Select the course name from the list and then write yes or no: ")


if userSelection == "Python Basic yes":
    print("Basic Python Course: Introduction to Python and Visual Studio Code. Variables, While and For Loops. You will learn about conditional instructions and put the knowledge you have gained into practice. At the end of the course you will take an exam.")
    print()
elif userSelection == "no":
    print()
elif userSelection == "Python intermediate yes":
    print("Intermediate Python course: This course is a continuation of. In the course you will learn things like GIT, classes and methods, lists, dictionaries, and arrays. APIs, and JSON Object Oriented Programming(OOP). Pygame library, Django, Random, Math, Introduction to Ethical Hacking, Introduction to Web development (Back-End). Final exam.")
    print()
elif userSelection == "no":
    print()
elif userSelection == "Python + AI":
    print("Python + AI course: In the course you will learn: Math library continued. Scikit-learn library, PyCaret, PyTorch, TensorFlow, Keras, FastAI, OpenCV, NumPy, SciPy, Matplotlib, Pandas. You will create your own machine learning AI model. Exam.")
    print()
elif userSelection == "no":
    print()
elif userSelection == "Start IT yes":
    print("Start IT course is a preparation for working as a Junior Python Developer or getting an internship! Course program: You choose a specialization from 5 available: Back-End developer, Tester, AI developer, Pentester or Django developer (WEB Developer). You will create your resume and 3 Machine Learning projects and 1 project in your specialty. Preparation for HR interview. PCEP or ISTQB exam.")
    print()
else:
    print("Ups!")
    
    
    
    print()
    
buy = int(input("Select the course number you want to buy. ATTENTION! REGARDLESS OF THE SELECTED COURSE NUMBER THE AMOUNT IS CALCULATED FOR 4 COURSES. PAYMENT FOR THE NEXT COURSE FOLLOWS AFTER PASSING THE EXAM. PAYMENT IN INSTALLMENTS POSSIBLE: "))



pythonBasic = buy * 300
pythonIntermediate = buy * 500
pythonAI = pythonIntermediate * 1000
startIT = pythonAI * 34
exam = startIT * 50
PCEP = exam * 100



print(pythonBasic) 
print(pythonIntermediate)
print(pythonAI)
print(startIT)
print(exam)
print(PCEP)



finalSum = pythonBasic + pythonIntermediate + pythonAI + startIT + exam + PCEP
print(finalSum)