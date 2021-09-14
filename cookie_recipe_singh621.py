"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Cookie Recipe
Date: 09/13/2021

Description:
    This program will have the user enter the number of cookies they would like
    to make make a ratio to 48 cokkies since we know ingredient amounts for 48.
    The the amounts will be multiplied by the ratio and retured in
    a print statement.

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

    cookies = int(input('How many cookies do you want to make? '))

    ratio = cookies/48 # finds the ratio of wanted cookie to recepie cook amount
    cs = 1.75*ratio #finds the cups of sugar
    cb = 1*ratio #finds the cups of butter
    cf = 2.5*ratio #finds the cups of flour
    #prints the amount of ingredients needed for specified cookie amount
    print(f'\nTo make {cookies} cookies, you will need: \n{cs:7.2f}'
    +f' cups of sugar\n{cb:7.2f} cups of butter\n{cf:7.2f} cups of flour')

if __name__ == '__main__':
    main()
