"""
Author: Jagroop Singh, singh621n@purdue.edu
Assignment: m.n - Fluid Mechanics
Date: 09/20/2021

Description:
    The program will take user entered temperature, velocty , and diameter and
    calculate and rutirn the Reynolds number

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


def main():
#inputs
    temp = float(input('Enter the temperature in °C as 5, 10, or 15: '))
    velocity = float(input('Enter the velocity of water in the pipe: '))
    diameter = float(input("Enter the pipe's diameter: "))
#viscosity assigned based on temp
    if temp == 5:
        viscosity = 1.49*10**-6
    elif temp == 10:
        viscosity = 1.31*10**-6
    elif temp == 15:
        viscosity = 1.15*10**-6

    renum = (velocity * diameter) / viscosity #reynolds number calc
    print(f'At {temp}°C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe \nis {renum: .2e}.')

if __name__ == '__main__':
    main()
