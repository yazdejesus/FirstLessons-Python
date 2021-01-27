import timeit as ti
import random as r
#user specifies number of questions (input for 'for loop')
reps = int(input('How many runs do you want? '))
i = 0
right = wrong = 0
#question is prompted to user and they respond there
for i in range(0,reps):
    num_a = r.randint(1,10)
    num_b = r.randint(1,10)
    result = num_a * num_b
    answer = int(input(f'What is the result of {num_a} * {num_b} ? '))
#response is evaluated 1. if is right or wrong (result stored) b. time taken (result stored)
    if answer != result:
        wrong += 1
    else:
        right += 1
    ratio = round((right/reps)*100,2)
#after all answers print "Thanks 4 playing" + number of right and wrong + % of rights
print (f"You had {reps} chances and only {right} answers correct: \n {ratio} % of correct answers")
#also show time to respond each and all
### additionally let user also specify how high the table should go and the results given