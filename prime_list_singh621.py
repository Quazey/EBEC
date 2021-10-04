"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Prime List
Date: 10/04/2021

Description:
    This program will print out a list of prime numbers where the 
    user enters a limit  and the numbers will be evaluated in is prime function till the limit.

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

    number = int(input('Enter a positive integer: ')) #ask for limit number
    print(f'The primes up to {number} are:', end='')
    for i in range(2,number+1): #loops from 2 to limit number
        result = is_prime(i) #calling prime function
        if result: #if prime numberthen list it
            print(f' {i},', end='') #print out the prime nums on same line


def is_prime(number):
    num = True #defult return
    if number == 2: #exception for 2
        return True
    else:
        for i in range(2, number): #checks for factors
            if (number % i) == 0:
                num = False
    return num #true or false

if __name__ == '__main__':
    main()
