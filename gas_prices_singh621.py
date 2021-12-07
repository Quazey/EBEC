"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Gas Prices
Date: 12/06/2021

Description:
    This program reads the contents of the txt file, and uses matplotlib to plot
    the data as a line graph.

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
    from matplotlib import pyplot as plt
    import numpy as np


    fo = open('2008_Weekly_Gas_Averages.txt','r') #opens file
    filecontent = fo.read() #reads
    ran_nums = filecontent.split('\n') #makes string an array at the new lines
    numlist = (ran_nums[0:len(ran_nums)-1]) #copy the same list of numes wothoit last element
    for i in range(0, len(numlist)): #converts elemesnts to floats
        numlist[i] = float(numlist[i])
    fo.close() #close file

    x = np.arange(52)#x values
    fig, ax = plt.subplots() #p;ots
    ax.plot(x+1, numlist)
    ax.set_xticks([10,20,30,40,50]) #set tick values
    ax.set_yticks([1.5,2.0,2.5,3.0,3.5,4.0])
    ax.grid()
    ax.set_title('2008 Weekly Gas Prices')
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_xlabel('Weeks (by number)')
    ax.set_xlim(1,52) #shifts boundaries
    ax.set_ylim(1.5,4.25)






    #plt.plot(x, y, color='r')
    plt.show()

if __name__ == '__main__':
    main()
