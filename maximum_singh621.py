"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Maximum
Date: 10/04/2021

Description:
    This program will create a comparing function and have it called in main
    . The function will accept 2 arguments and compare to see which is greater.
    It will return the greater value.

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

    first = input('Enter the first integer: ') #output set up
    second = input('Enter the second integer: ') #output set up
    max = max_of_two(first, second) #calling max function
    print(f'The number {max} is greater.') #output print

def max_of_two(a,b):#max number function

    if a > b: #check if a isgreater than b
        return a
    else: #returns max
        return b

if __name__ == '__main__':
    main()
