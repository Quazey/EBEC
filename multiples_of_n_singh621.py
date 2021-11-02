"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Multiples of N
Date: 11/01/2021

Description:
    This program will call a function and create a list of muultiples
    using a parameter and return that list.

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
    og_list = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406] #given list
    mult_num = 13 #gicen number
    new_list = multiples_of(mult_num,og_list) #calling function
    print(f'Original list of numbers:\n  {og_list}') #print statements
    print(f'Numbers in the list that are multiples of 13:\n  {new_list}')

def multiples_of(a, b): #function definintion
    new_list = list() #new empty list
    for e in range(0,len(b)): #finding multiples
        if b[e] % a == 0:
            new_list.append(b[e])
    return new_list #returningnew list

if __name__ == '__main__':
    main()
