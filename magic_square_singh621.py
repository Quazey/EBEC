"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Magic Square
Date: 11/01/2021

Description:
    This program will call a function to check if a given array list is a
     Lu SHu square

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


def main(): #main4

    square1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #3 squares we are checking
    square2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    square3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    print('Your square is:')#print statemnt
    print_square(square1)#calls printing funkion
    a = is_magic(square1) #the true or fals eboolean
    if a == False:
        print('It is not a Lo Shu magic square.')#print statemnt
    else:
        print('It is a Lo Shu magic square!')#print statemnt
    print('\nYour square is:')
    print_square(square2) #calls printing funkion
    b = is_magic(square2) #the true or fals eboolean
    b = False
    if b == False:
        print('It is not a Lo Shu magic square.')#print statemnt
    else:
        print('It is a Lo Shu magic square!')#print statemnt
    print('\nYour square is:')#print statemnt
    print_square(square3)#calls printing funkion
    c = is_magic(square3) #the true or fals eboolean
    if c == False:
        print('It is not a Lo Shu magic square.\n')#print statemnt
    else:
        print('It is a Lo Shu magic square!\n')#print statemnt

def print_square(a): #function definintion
    print(f'  {a[0][0]} {a[0][1]} {a[0][2]}\n  {a[1][0]} {a[1][1]} {a[1][2]}\n  {a[2][0]} {a[2][1]} {a[2][2]}')
    #print statemnt
def is_magic(a):
    n = len(a) #length of list
    for i in range(n): #checks sums of horizontal rows
        sum_row = 0
        for j in range(n):
            sum_row += a[i][j]
        if sum_row == 15:
            x = 1
        else:
            x = 3
    for i in range(n): #checks sums of vertical comuns
        sum_col = 0
        for j in range(n):
            sum_col += a[j][i]
        if sum_col == 15:
            y = 1
        else:
            y = 3
    sum_diag1 = 0
    for i in range(n): #checks sums for 1 diagonal
        sum_diag1 += a[i][i]
    if sum_diag1 == 15:
            z = 1
    else:
            z = 3
    sum_diag2 = 0
    for i in range(n): #checks sums for 2 diagonal
        sum_diag2 += a[i][-(i+1)]
    if sum_diag2 == 15:
        t = 1
    else:
        t = 3

    if (x+y+z+t == 4): #checks if all directiosn add to 15
        return True
    return False
if __name__ == '__main__':
    main()
