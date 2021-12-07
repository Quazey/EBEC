"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n - Sin Cos
Date: 12/06/2021

Description:
    This program will program that uses matplotlib to draw a plot of sine and
    cosine from 0 to 2π on the same axes. It includes x-axis tick marks every π2
    and y-axis tick marks at -1 and 1. Color the sine wave red and the cosine
    wave blue.

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
    x = np.arange(0,2*np.pi+.05,.1)   # start,stop,step for x alues
    y = np.sin(x) #sine values
    z = np.cos(x) #cos y values
    #plots figures
    fig, ax = plt.subplots()
    plt.plot(x, y, color='r')
    plt.plot(x, z, color='b')
    ax.set_xticks([np.pi/2,np.pi,3*np.pi/2,2*np.pi]) #set tick values
    ax.set_yticks([-1,1])
    xlabels = ['$\pi/2$','$\pi$', '$3\pi/2$', '$2\pi$'] #set tick label
    ax.set_xticklabels(xlabels)
    #adds spines 
    for spine in ['top', 'right']:
         ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
         ax.spines[spine].set_position('zero')
    plt.show()

        #plots the fugures


if __name__ == '__main__':
    main()
