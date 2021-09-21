"""
Author: Jagroop Singh, singh621n@purdue.edu
Assignment: m.n - Software Sales
Date: 09/20/2021

Description:
    The program will take a package number to be purchased, check if the input
    is valid and then return the discount applied and price.

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
    price = 79 #pice of single package
    #ask for input of package
    package = int(input('How many packages will be purchased: '))
    if (package < 0): #checks to see if negative
            print('  Invalid Input!')
    elif (package >= 100): #checks is number of packages is less than 100,50,25,5
        cost = (1-.45)*price*package
        print('  45% discount applied.')
        print(f'  The total price for purchasing {package} packages is ${cost:,.2f}.')
    elif (package >= 50): 
        cost = (1-.3)*price*package
        print('  30% discount applied.')
        print(f'  The total price for purchasing {package} packages is ${cost:,.2f}.')
    elif (package >= 25): 
        cost = (1-.2)*price*package
        print('  20% discount applied.')
        print(f'  The total price for purchasing {package} packages is ${cost:,.2f}.')
    elif (package >= 5): 
        cost = (1-.1)*price*package
        print('  10% discount applied.')
        print(f'  The total price for purchasing {package} packages is ${cost:,.2f}.')
    else: #defualt prints and cost formula
        cost = price * package
        print('  No discount applied.')
        print(f'  The total price for purchasing {package} packages is ${cost:,.2f}.')





if __name__ == '__main__':
    main()
