"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  Number Writer
Date: 11/15/2021

Description:
    This program will at asks the user how many numbers it should generate and
    then writes that many random numbers to a file.

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
    import random
    amount = int(input('How many numbers would you like? ')) #user input
    counter = 0 #counter
    fo = open('random_numbers.txt','w') #opens file and creates on first run
    while (counter < amount): #while loop that runs the user specifed amount
        fo.write(str(random.randrange(1019,1216))) #generates random nmber in parameters
        fo.write('\n') #new line
        counter = counter + 1
    fo.close() #closes file

if __name__ == '__main__':
    main()
