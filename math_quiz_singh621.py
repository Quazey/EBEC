"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Math Quiz
Date: 10/19/2021

Description:
    This program will create a summing math probelm for the user using random
    function.

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

    a, b = 2, 3
    twodigit = random_number(a) #calling for 2 digit random numnber
    threedigit = random_number(b) #calling for 3 digit randpm nimber
    print(f'{twodigit:5}') #setting up printing output
    print(f'+ {threedigit:3}')
    print('-----')
    useranswer = int(input('= ')) #asking for fer answer
    correctanswer = twodigit + threedigit #correct answer
    if useranswer == (correctanswer): #comapring
        print('Correct -- Good Work!') #print if correect
    else:
        print(f'Incorrect. The correct answer is {correctanswer}.') #prints if wrong

def random_number(a):#random number function with digit num max a parameter
    import random #import module
    b = a-1 #min number of digits
    lower = 10**b #lower numberbound
    upper = 10**a #upper number bound
    c = random.randrange(lower,upper) #calls random range function for random module
    return c

if __name__ == '__main__':
    main()
