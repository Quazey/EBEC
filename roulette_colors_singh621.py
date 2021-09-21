"""
Author: Jagroop Singh, singh621n@purdue.edu
Assignment: m.n - Roulette Colors
Date: 09/20/2021

Description:
    The program will take a pocket number 1-36 from the user, check if the input
    is valid and then return the pocket number with the color.

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


def main():

    pocket = int(input('Please choose a pocket number: '))
    if (pocket < 0) or (pocket > 36): #checks to see if pocket is 1-36
            print('  Invalid Input!')
    elif (pocket >= 29): #checks the pocket number in given sections
        if (pocket % 2 == 0):
            print(f'  Pocket number {pocket} is red.')
        else:
            print(f'  Pocket number {pocket} is black.')
    elif (pocket >= 19):
        if (pocket % 2 == 0):
            print(f'  Pocket number {pocket} is black.')
        else:
            print(f'  Pocket number {pocket} is red.')
    elif (pocket >= 11):
        if (pocket % 2 == 0):
            print(f'  Pocket number {pocket} is red.')
        else:
            print(f'  Pocket number {pocket} is black.')
    elif (pocket >= 1):
        if (pocket % 2 == 0):
            print(f'  Pocket number {pocket} is black.')
        else:
            print(f'  Pocket number {pocket} is red.')
    else: # zero pocket seperate print
            print(f'  Pocket number {pocket} is green.')

if __name__ == '__main__':
    main()
