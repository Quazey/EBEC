"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Star Pattern
Date: 10/11/2021

Description:
    This program will make a user ented number sided star that is filled
     with color.

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    """Write your code below this line."""
    side_length = 60 #line length
    points = int(input("Please enter how many points the star will have?  ")) #number of points on star
    innerang = 360 / points #concave angle
    outerang = 2 * innerang #inner angle
    color('black', 'blue') #line and fill color
    right((180-outerang)/2) #sets the trutle orientation from zero to desired start angle
    begin_fill() #adds the color
    for a in range(points): #turtle movement
        forward(side_length)
        left(180-innerang)
        forward(side_length)
        right(180-outerang)
    end_fill()
# Do not change anything after this line.
if __name__ == '__main__':
    start()
    main()
    done()
