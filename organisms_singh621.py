"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Organisms
Date: 09/27/2021

Description:
    This program will ask the user to enter a start population, a growth rate,
    and number of days for growth. it will list aout the growth per day across
    the designated period.

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

    start = float(input('Starting number, in million: ')) # inputs
    rate = float(input('Average daily increase, in percent: '))
    days = int(input('Number of days to multiply: '))
    print('Day   Approx. Pop') #heading print statement
    for n in range(days+1): #settibg for loop
        print(f'{n:3} {start:13.4f}') #print reult with formatting
        start = start * ((rate/100)+1) #math calculation

if __name__ == '__main__':
    main()
