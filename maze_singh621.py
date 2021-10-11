"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Maze
Date: 10/11/2021

Description:
    This program will import a maze picture and have turtle navigate out of
     the maze.

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

from turtle import *

def start():
    """This function initializes the window and the turtle.
    Do not modify this function.
    """
    setup(564, 564)
    bgpic('mazey.png')
    shape('turtle')
    color('green')
    width(5)

def main():
    """Write your code below this line."""

right(90)
forward(10)
left(90)
forward(35)
left(90)
forward(45)
right(90)
forward(50)
right(90)
forward(20)
left(90)
forward(45)
right(90)
forward(27)
left(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(65)
right(90)
forward(30)


# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
