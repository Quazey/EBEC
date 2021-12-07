"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Covid 19 Cases
Date: 12/06/2021

Description:
    This program  reads the contents of the file and calculates the total number
    of positive results for each day by summing all of the positive results
    prior to and including that day. Then, using matplotlib, plot the total
    number of positive cases for each day as a bar chart.

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


    fo = open('indiana_covid_19_data_fall_2021.txt','r') #opens file
    filecontent = fo.read() #reads
    case_data = filecontent.split('\n') #makes string an array at the new lines

    numlist = (case_data[0:len(case_data)-1]) #copy the same list of numes wothoit last element

    for i in range(0, len(numlist)): #converts elemesnts to floats
        a = numlist[i].split(' ')
        numlist[i] = a
    fo.close() #close file
    y = [0]*len(numlist)
    for i in range(1, len(numlist)): #converts elemesnts to floats
        y[i] = float(numlist[i][2])/1000+ y[i-1]

    x = np.arange(len(numlist))#x values
    fig, ax = plt.subplots() #p;ots
    ax.bar(x, y)
    ax.set_xticks([5,66,127,189,250,311,370,431,492,554,611]) #set tick values
    ax.set_yticks([0,200,400,600,800,1000,1200])
    dates = ['2020-03','2020-05','2020-07','2020-09','2020-11','2021-01','2021-03','2021-05','2021-07','2021-09','2021-11']
    ax.set_xticklabels(dates)
    fig.autofmt_xdate()

    ax.grid()
    ax.set_title('Positive COVID-19 Cases in Indiana')
    ax.set_ylabel('Number of Cases (in thousands)')
    ax.set_xlabel('Date')
#    ax.set_xlim(1,52) #shifts boundaries
#    ax.set_ylim(1.5,4.25)






    #plt.plot(x, y, color='r')
    plt.show()

if __name__ == '__main__':
    main()
