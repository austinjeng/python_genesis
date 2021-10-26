from math import e
import os
import random

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#print(__location__)

def getUserScore(userName):
    try: 
        f = open(os.path.join(__location__, 'userScores.txt'), 'r')
        content = []
        for line in f:
            content = line.split(', ')
            if content[0] == userName:
                f.close()
                return content[1]
        
        f.close()
        return -1
    except IOError:
        print('File is not found') 
    input.close()

def updateUserPoints(newUser, userName, score):
    if newUser:
        input = open(os.path.join(__location__, 'userScores.txt') , 'a')
        input.write(f'\n{userName}, {score}')
        input.close() 

    if not newUser:
        input = open(os.path.join(__location__, 'userScores.txt') , 'r')
        output = open('userScores.tmp', 'w')
        for line in input:
            content = line.split(", ")
            if content[0] == userName:
                content[1] = score
                line = f'{content[0]}, {content[1]}\n'
            output.write(line)
        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')
        input.close()
        output.close()

operandList = [0, 0, 0, 0, 0]
operatorList = ['','','','']

operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

for i in range(5):
    operandList[i] = random.randint(1, 9)

for i in range(4):
    if i > 0 and operatorList[i - 1] != '**':
        operatorList[i] = operatorDict[random.randint(1,4)]
    else :operatorList[i] = operatorDict[random.randint(1,3)]
    
questionString = ''
for i in range(4):
    questionString = questionString + str(operandList[i]) + str(operatorList[i])
questionString = questionString + str(operandList[4])

result = eval(questionString)

questionString = questionString.replace('**', '^')

'''
while True:
    try:
        userInput = int(input('Enter the answer of' + questionString + ': '))
        if userInput == result:
            print('Congradulations, you are Correct. The answer is', result)
            break
        else: 
            print('Incorrect answer, try again!') 
    except Exception:
        print('Incoreect format. The input should be in type Integer!')
'''




updateUserPoints(True, 'Keven', 87)

#print(getUserScore("Carol"))
