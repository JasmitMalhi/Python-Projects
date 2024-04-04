import random
import time

OPERATORS=["+","-","*"]
MIN_OPERAND=3
MAX_OPERAND=12
TOTAL_PROBLEMS=10
def generateProblem():
    left=random.randint(MIN_OPERAND, MAX_OPERAND)
    right=random.randint(MIN_OPERAND, MAX_OPERAND)
    operator=random.choice(OPERATORS)
    #
    expr=str(left)+" "+operator+" "+str(right)
    answer=eval(expr)#evualtes string as if it is a pyhton expression
    return expr,answer
expr,answer=generateProblem()
print(expr,answer)


wrong=0
input("Press enter to start! ")
print("--------------------------------")
start_time=time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer=generateProblem()
    while True:
        guess=input("Problem # "+str(i+1)+": "+expr+" = ")#The problem number
        if guess ==str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=end_time+start_time
print("--------------------------------")
print("Nice work! you finished in ", total_time," seconds!")
