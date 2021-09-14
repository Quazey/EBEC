"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Interest
Date: 09/13/2021

Description:
    This program will calculate and return compound interest by asking for the
     principle amount, numbers of times coumpounded, the interest rate in
      percent, and the number of years the money was left in the account.

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
    #asked user to input quantities
    print('Please enter the following quantities.')
    #assigns quantities to variables
    P = int(input('  How much is the initial deposit? '))
    r = float(input('  What is the annual interest rate in percent? '))
    n = int(input('  How many times per year is the interest compounded? '))
    t = float(input('  How many years will the account earn interest? '))

    FV = P*(1 +((r/100)/n))**(n*t) #solves for compoundednd Interest
    #print Statementstated amount and in how many years
    print(f'\nAt the end of {t} years, this account will be worth ${FV:,.2f}.')

if __name__ == '__main__':
    main()
