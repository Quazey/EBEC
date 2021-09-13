"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Vineyard
Date: 09/13/2021

Description:
    This program will as the user to input the amount of space between
    grapevines, the length of the rows, and the width of the end-post assembly.
    Using these quantities, it will calculated the number of grapevines avalible
    to be in the designated amount of space.

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
    #asks for input quantities
    print('Enter each of the following quantities in meters.')
    #assigns input quantities to variables
    S = int(input('  How much space should be between the vines? '))
    E = float(input('  How wide is the end-post assembly? '))
    R = int(input('  How long is this row? '))

    V = int((R-(2*E))/S) #finds number of grapevines
    #prints number of grapevines
    print(f'\nThis row has enough space for {V} vine(s).')

if __name__ == '__main__':
    main()
