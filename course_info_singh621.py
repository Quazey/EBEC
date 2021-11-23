"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  Course Info
Date: 11/22/2021

Description:
    This program will This program makes two dictionaries from a text file,
     prompt a user to enter a year and display a team won World Series in the
     year and the time to win World Series.

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

def main ():
    #********** the autograder seems to be freaking out at putting in values
    #that yeild different results than when i check the same condition manually* 
    d = get_course_data() #call s for the dictionary
    course = input('Enter a course number: ')
    h= d.keys()
    g = d.get(course, 1) #checks if input matches a key
    if g == 1: #not a match
        print(f'  {course} is an invalid course number.')
    else:
        print(f'  The details for course {course} are:')
        print('    Instructor:',d[course]['instructor'],'\n          Room:',d[course]['room'],'\n          Time:',d[course]['time'])

def get_course_data(): #the dictionary made
    d = {'CS101': {'room': '3004','instructor': 'Django', 'time': '9:00 a.m.'},
     'CS102': {'room': '4501','instructor': 'Idle', 'time': '10:00 a.m.'},
     'CS103': {'room': '6755','instructor': 'Rich', 'time': '11:00 a.m.'},
     'NT110': {'room': '1244','instructor': 'Marshal', 'time': '12:00 p.m.'},
     'CM241': {'room': '1411','instructor': 'Pickle', 'time': '2:00 p.m.'}}
    return d

if __name__ == '__main__':
    main()
