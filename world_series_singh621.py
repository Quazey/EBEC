"""
Author: Jagroop Singh, singh621@purdue.edu
Assignment: m.n -  World Series
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

def main():
    champ_dict, numb_dict = load_winners_data() #gets dictionaries
    year = int(input('Enter a year in the range 1903 -- 2020: ')) #input
    if year > 1902 and year < 2021 and year != 1904 and year != 1994: #conditional print statmrnts
        print(f'  The {champ_dict[year]} won the World Series in {year}.\n  They have won the World Series {numb_dict[champ_dict[year]]} times.')
    elif year == 1904:
        print("  The World Series wasn't played in the year 1904.")
    elif year == 1994:
        print("  The World Series wasn't played in the year 1994.")
    else:
        print(f'  Data for the year {year} is not included in this system.')

def load_winners_data():
    # make two dictionaries
    champ_dict = {}
    fo = open('WorldSeriesWinners.txt','r') #opens file, reads, close
    filecontent = fo.read() #reads
    line = filecontent.split('\n')
    fo.close()

    m = 0
    champ_dict[1903] = line[m]
    #for loop ranges made 3times to exclude the yeats with no data
    for i in range(1905,1994):
        m = m+1
        champ_dict[i] = line[m]
    for i in range(1995, 2021):
        m = m+1
        champ_dict[i] = line[m]
    numb_dict = {}
    for i in range(1903, 1904):
        team = champ_dict[i]
        if not team in numb_dict:
            numb_dict[team] = 1
        else:
            numb_dict[team] += 1
    for i in range(1905, 1994):
        team = champ_dict[i]
        if not team in numb_dict:
            numb_dict[team] = 1
        else:
            numb_dict[team] += 1
    for i in range(1995, 2021):
        team = champ_dict[i]
        if not team in numb_dict:
            numb_dict[team] = 1
        else:
            numb_dict[team] += 1
    return champ_dict, numb_dict

if __name__ == '__main__':
    main()
