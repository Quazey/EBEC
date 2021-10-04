"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Avg Grade
Date: 10/04/2021

Description:
    This program will create a contain 3 differnt functions that ask for a
    valid score, calculate the average of the scores, and determin the grade.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main(): #main
    scores = [0,0,0,0,0] #empty score list
    i = 0 #counter
    while i < 5:
        scores[i] = get_valid_score() #calling scores
        grade = determine_grade(scores[i]) #calling grades
        print(f'  The letter grade for {scores[i]} is {grade}.')
        i+=1 #incrementing
    avg = calc_average(scores) #calling average
    grade = determine_grade(avg) #grade for average
    print('\nResults:')
    print(f'  The average score is {avg:.2f}.')
    print(f'  The letter grade for {avg:.2f} is {grade}.')


def get_valid_score():
    score = float(input('Enter a score: ')) #asking user in enter score
    while score < 0 or score > 100: #setting bounds
        print('  Invalid input. Please try again') #asking for valid input
        score = float(input('Enter a score: '))
    return score

def calc_average(a):
    sum = 0 #intializze variables
    counter = 0
    for i in a:
        sum = sum + i #running sum of scores
        counter += 1 #counter in loop
    return sum/counter

def determine_grade(percent):
    if percent >= 91:#comparing percent to find grade via if else statemtnes
        return 'A'
    elif percent >= 82:
        return 'B'
    elif percent >= 73:
        return 'C'
    elif percent >= 64:
        return 'D'
    else: #defult return
        return 'F'



if __name__ == '__main__':
    main()
