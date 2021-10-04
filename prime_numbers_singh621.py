"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Prime Numbers
Date: 10/04/2021

Description:
    This program will create a contain a bolean function that will return true
    or false if a given argument is a prime or normal number. It will do this
    until user quits the program.

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
    number = 0
    while number != -1:
        number = int(input('Enter a positive integer (-1 to quit): '))
        result = is_prime(number)
        if number != -1 :
            if result:
                print(f'  {number} is a prime.')
            else:
                print(f'  {number} is not a prime.')

def is_prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if (number % i) == 0:
                return False
            else:
                return True

if __name__ == '__main__':
    main()
