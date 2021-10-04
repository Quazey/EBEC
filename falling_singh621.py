"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Falling
Date: 10/04/2021

Description:
    This program will create a computational function and have it called in main
    . The function will calculate the distance an object has fallen given a time
    argument from main.

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

    print('Time (s)  Distance (m)') #output set up
    print('----------------------') #output set up
    for t in range(5,51,5): #for loop of time in s
        d = falling_dist(t)
        print(f'{t:8} {d:13.1f}')

def falling_dist(time):#dalling distance function

    g = 8.87 #gravity m/s*s
    d = .5*g*time**2 #distance formula m
    return d

if __name__ == '__main__':
    main()
