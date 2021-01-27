import timeit as ti
import random as r
#user specifies number of questions (input for 'for loop')
reps = int(input('How many runs do you want? '))
limite = int(input('Define maximum multiplication number: '))
i = 0
right = wrong = 0
result = 1
answer = 0
right_answers = {}
wrong_answers = {}
#encapsulate logic in a function
def rand_calc():
    global result, answer, num_a, num_b
    num_a = r.randint(1,limite)
    num_b = r.randint(1,limite)
    result = num_a * num_b
    answer = int(input(f'What is the result of {num_a} * {num_b} ? '))
    return answer, result, num_a, num_b
#response is evaluated 1. if is right or wrong (result stored) b. time taken (result stored)
if limite not in range(1,100):
    limite = int(print('Select a number between 1 and 100'))

for i in range(0,reps):
    rand_calc()
    desc = str(num_a) + ' * ' + str(num_b)
    if answer != result:
        wrong += 1
        wrong_answers[desc] = answer
    else:
        right += 1
        right_answers[desc] = answer
    ratio = round((right/reps)*100,2)  

print (f"You had {reps} chances, {right} correct answers: \n {ratio} % accuracy. \n Your wrong answers were {wrong_answers}")
#also show time to respond each and all
### additionally let user also specify how high the table should go and the results given