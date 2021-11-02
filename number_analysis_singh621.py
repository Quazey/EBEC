"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Number Analysis
Date: 11/01/2021

Description:
    This program will call a function to ask the user for 10 numbers and will
    return the min, max, toal, and average.

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


def main(): #main4


    print('Enter 10 numbers:')
    b = get_number_list()
    maxL = max(b) #max of list
    minL = min(b) #min of list
    sumL = sum(b) #sum of list
    avgL = sumL / len(b) #average of list
    #print statemnts
    print(f'Highest number: {maxL:.2f}')
    print(f'Lowest number: {minL:.2f}')
    print(f'Total: {sumL:.2f}')
    print(f'Average: {avgL:.2f}')

def get_number_list(): #function definintion
    a = 1 #counter
    c = list()
    while a < 10: #loop call for input
        b = float(input(f'  number  {a} of 10: ')) #input statemnt
        c.append(b)
        a = a + 1
    b = float(input(f'  number 10 of 10: ')) #input statemnt for 10 due to spacing
    c.append(b)
    return c #returns user number


if __name__ == '__main__':
    main()
