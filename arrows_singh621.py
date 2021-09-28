"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Arrows
Date: 09/27/2021

Description:
   
    This program will ask the user for a number and return that number of Arrows
    in a row coloum incemented format.

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

    arrows = int(input('How many arrows should I draw? ')) #asks user for number of arrows
    for i in range(arrows): #outside for loop for rows
        print('<', end = "")
        for j in range(i): #inner for loop for columns
            print('-',end = "") #varies the number of dashes for the arroe
        print('>')

if __name__ == '__main__':
    main()
