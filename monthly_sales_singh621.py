"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Monthly Sales
Date: 12/06/2021

Description:
    This program will collects monthly sales data from the user and stores it
    in a list and then use matplotlib to plot the sales values as a pie chart.

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
    #asks user for input amount
    jan = input('Enter the sales for January: ')
    feb = input('Enter the sales for February: ')
    mar = input('Enter the sales for March: ')
    apr = input('Enter the sales for April: ')
    may = input('Enter the sales for May: ')
    jun = input('Enter the sales for June: ')
    jul = input('Enter the sales for July: ')
    aug = input('Enter the sales for August: ')
    sep = input('Enter the sales for September: ')
    oct = input('Enter the sales for October: ')
    nov = input('Enter the sales for November: ')
    dec = input('Enter the sales for December: ')
    #makes input amounts into lists
    months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    #makes a list of month names
    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #plots the fugures
    fig, ax = plt.subplots()
    ax.set_title('Monthly Sales Values') #title
    c = ('#4D4038','#BAA892','#5B6870','#6E99B4','#A3D6D7','#085C11','#849E2A','#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A')
    ax.pie(months, colors=c, labels=monthNames) #pie chart with data from months, color , and the month labels
    plt.show()


if __name__ == '__main__':
    main()
