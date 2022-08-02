# Author(s): Eric Mossotti, Colby Ackerman
# About: Red or Black - Gathering data

from random import choice
import pandas as pd


def colorChoice(blks, reds, n):

    i = 0

    # the two possibilities which will be used for easy readability in the data frame
    possibilities = ['red', 'black']

    # loop iterates until i equals number of rounds specified by the user
    while i < n:

        # bot choice using random data generator aka jenny
        botsChoice = choice(possibilities)

        if botsChoice == 'red':
            reds = reds + 1

        else:
            blks = blks + 1

        # updates how many turns have passed for the while loop
        i += 1

# MAIN
def main():

    # creates placeholder variables to hold values corresponding to them randomly,
    # and automatically, generated data for red and black values
    blks = 0
    reds = 0


    # user specifies number of rounds n
    n = int(input("Enter how many rounds n: "))

    # DATA GENERATION STEP
    colorChoice(blks, reds, n)


    # creates a dictionary of the randomly generated inputs
    bot_dict = {'Bot': ['Bot'],
                   'Reds': [reds],
                   'Blacks': [blks]}

    # creates an empty dataframe
    bot_df = pd.DataFrame(bot_dict)

    # fills in the dataframe in accordance with the dictionary that was created previously
    bot_df = bot_df.set_index('Bot')

    # test print of the dataframe to confirm that the dataframe was successfully created
    print("\n",
          bot_df)

    # Create a .CSV File From User Input

    # takes input from user
    filepath = str(input("\n"
                         "To create and save a .CSV file of your dataframe\n"
                         "please enter the desired filepath along with the name of the file.\n"
                         "Do not input quotes. Use single backslashes.\n"
                         "e.g.: C:\\folder\\subfolder\\filename.csv"
                         "\n" ))

    # creates a file of a user specified path
    redBlackData = open(filepath, "x")

    # saves the dataframe information to the newly created .CSV file
    bot_df.to_csv(redBlackData)

if __name__ == '__main__':
     pass
