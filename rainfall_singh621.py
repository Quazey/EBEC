"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Rainfall
Date: 09/27/2021

Description:
    This program will ask the user to enter number of years and then number
    rainfall for the month. It will return an average of rain fall if all
     inputs ar valid if not it will ask again.

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
    sum, count, avg = 0, 0, 0 #intialize variables
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    years = (int(input('Enter the number of years: '))) #number of years input
    if years < 1: #check to see if years is valid
        print('Invalid input.')
    for n in range(years): #cycles through number of years
        print(f'  For year No. {years}')
        for i in months:#cycles through all 12 months
            count += 1 #counter
            rain = float(input(f'    Enter the rainfall for {i}.: ')) #user rainfall amount input
            while rain < 0: #invalid input check
                print('    Invalid input, please try again.')
                rain = float(input(f'    Enter the rainfall for {i}.: '))
            sum = sum + rain #summing rainfall
    if years >= 1: #if valid print statemnts
        print(f'There are {count} months.')
        print(f'The total rainfall is {sum:.2f} inches.')
        print(f'The monthly average rainfall is {(sum/count):.2f} inches.')

if __name__ == '__main__':
    main()
