"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  Pig Latin
Date: 11/08/2021

Description:
    This program will take a string imput and make it into pig latin and return
    it for the user.

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
    userstrng = input('Enter a string: ') #user input string
    pigstrng = pig(userstrng) #function call
    print('Pig latin: ' + pigstrng) #print output

def pig(a):
    wordsog = a.lower().split() # makes lowercase string and splits into parts for list
    pigparts = [] * (len(wordsog)+1) #empty array
    for i in wordsog:
        if i == wordsog[0]:
            b = i[1].upper() + i[2:len(i)] + (i[0])+'ay' #rearrgaes word
            pigparts.append(b)
        else:
            b = i[1:len(i)]+ (i[0])+'ay'
            pigparts.append(b)
    pigstrng = ' '.join(pigparts) #joins list words into string
    return pigstrng #returns pig latin string

if __name__ == '__main__':
    main()
