"""
Author: Jagroop Singh, singh621n@purdue.edu
Assignment: m.n - Leap Year
Date: 09/20/2021

Description:
    The program will take a year input from the user and determine if the Year
    is a leap year or not and tell the user the result.

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

    Year = int(input('Please input a year: ')) #ask for input of year
    if not (Year % 100): #checks to see if divisoble by 100
        if not (Year % 400): #check for 400 divisibilty in nested way
            print(f'In the year {Year}, February has 29 days.')
        else: #if not true then reutrn the other print statement
            print(f'In the year {Year}, February has 28 days.')

    elif not (Year % 4): #checks 4 divibility if not divisible by 100
        print(f'In the year {Year}, February has 29 days.')
    else: #print statement depended in true or false
        print(f'In the year {Year}, February has 28 days.')

if __name__ == '__main__':
    main()
