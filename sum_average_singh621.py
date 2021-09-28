"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Sum Average
Date: 09/27/2021

Description:
    This program will ask the user for a postive or zero number and return
    the sum of the entered numbers. It will check for a valid input and
     terminate when encountering a negative number.

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
    value, sum, count, average = 0, 0, 0, 0 #intialize variables
    while value >= 0: #while input is positve loop
        count += 1 #counter
        sum = sum + value #summing
        value = float(input('Enter a non-negative number (negative to quit): '))
    if sum == 0 and value < 0 : #invalid input of first number
        print("  You didn't enter any numbers.")
    else: #standard print statments
        print(f'  You entered {count-1} numbers.')
        print(f'  Their sum is {sum:.3f} and their average is {(sum/(count-1)):.3f}.')
if __name__ == '__main__':
    main()
