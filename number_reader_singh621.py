"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  Number Reader
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
    fo = open('random_numbers.txt','r') #opens file
    filecontent = fo.read() #reads
    ran_nums = filecontent.split('\n') #makes string an array at the new lines
    numlist = (ran_nums[0:len(ran_nums)-1]) #copy the same list of numes wothoit last element to convert int
    for x in range(0,len(numlist)): #loop converts ints
        numlist[x] = int(numlist[x])
    a = min(numlist) #min
    b = max(numlist) #max
    c = len(numlist) #length
    d = sum(numlist) #sum
    #print(numlist)
    fo.close() #close file
    print(f'{c:,} numbers were read from the file.') #print statements
    print(f'Min: {a:,}')
    print(f'Max: {b:,}')
    print(f'Sum: {d:,}')
    print(f'Avg: {(d/c):,.1f}')

if __name__ == '__main__':
    main()
