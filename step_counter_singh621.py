"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  Step Counter
Date: 11/15/2021

Description:
    This program will read a tect file and return steps for each month.

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
    fo = open('steps.txt','r') #opens file
    filecontent = fo.read() #reads
    numlist = filecontent.split('\n') #makes string an array at the new lines
    fo.close() #close file
    for x in range(0,len(numlist)-1): #convert string to int
        numlist[x] = int(numlist[x])
    
    jansum = sum((numlist[0:31])) #finds sum
    janavg = jansum / 31 #find average
    febsum = sum((numlist[31:59])) #finds sum
    febavg = febsum / 28 #find average
    marsum = sum((numlist[59:90])) #finds sum
    maravg = marsum / 31 #find average
    aprsum = sum((numlist[90:120])) #finds sum
    apravg = aprsum / 30 #find average
    maysum = sum((numlist[120:151])) #finds sum
    mayavg = maysum / 31 #find average
    junsum = sum((numlist[151:181])) #finds sum
    junavg = junsum / 30 #find average
    julsum = sum((numlist[181:212])) #finds sum
    julavg = julsum / 31 #find average
    augsum = sum((numlist[212:243])) #finds sum
    augavg = augsum / 31 #find average
    sepsum = sum((numlist[243:273])) #finds sum
    sepavg = sepsum / 30 #find average
    octsum = sum((numlist[273:304])) #finds sum
    octavg = octsum / 31 #find average
    novsum = sum((numlist[304:334])) #finds sum
    novavg = novsum / 30 #find average
    decsum = sum((numlist[334:365])) #finds sum
    decavg = decsum / 31 #find average
    #print statments
    print('The average steps taken each month were:\n   January : {janavg:.2f}\n  February : {febavg:.2f}\n     March : {maravg:.2f}\n     April : {apravg:.2f}\n       May : {mayavg:.2f}\n      June : {junavg:.2f}\n      July : {julavg:.2f}\n    August : {augavg:.2f}\n September : {sepavg:.2f}\n   October : {octavg:.2f}\n  November : {novavg:.2f}\n  December : {decavg:.2f}')



if __name__ == '__main__':
    main()
