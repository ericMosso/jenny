# Author(s): Eric Mossotti, Colby Ackerman
# About: Red or Black - Gathering data
from random import choice
import pandas as pd

# creates placeholder variables to hold values corresponding to the randomly,
# and automatically, generated data for red and black values
blkBot = 0
redBot = 0

# placeholder values for manually inputted red and black values
blkMan = 0
redMan = 0

# the two possibilities which will be used for easy readbility in the data frame
possibilities = ['red', 'black']

# user specifies number of rounds n
n = int(input("Enter how many rounds n: "))

# DATA GENERATION STEP

# counter set to 0 initially
i = 0

# loop iterates until i equals number of rounds specified by the user
while i < n:
    # bot choice using random data generator aka jenny
    botsChoice = choice(possibilities)
    if botsChoice == 'red':
        redBot = redBot + 1
    else:
        blkBot = blkBot + 1

    # just a basic proof of concept

    # manual input for red
    x = input("Red or black? (type r for red or b for black): ")

    # manual input for red
    if x == 'r':
        redMan = redMan + 1

    # inputs of b along with any errors in input
    # are simply going to register as black for now
    else:
        blkMan = blkMan + 1  # manual input for black

    # updates how many turns have passed for the while loop
    i += 1

# creates a dictionary of the manual and randomly generated inputs
manbot_dict = {'Man|Bot': ['Bot', 'Man'],
               'Reds': [redBot, redMan],
               'Blacks': [blkBot, blkMan]}

# creates an empty dataframe
manbot_df = pd.DataFrame(manbot_dict)

# fills in the dataframe in accordance with the dictionary that was created previously
manbot_df = manbot_df.set_index('Man|Bot')

# test print of the dataframe to confirm that the dataframe was successfully created
print("\n",
      manbot_df)

# Create a .CSV File From User Input

# takes input from user
filepath = str(input("\n"
                     "To create and save a .CSV file of your dataframe\n"
                     "please enter the desired filepath along with the name of the file.\n"
                     "Do not input quotes. Use single backslahses.\n"
                     "e.g.: C:\\folder\\subfolder\\filename.csv"
                     "\n" ))

# creates a file of a user specified path
redBlackData = open(filepath, "x")

# saves the dataframe information to the newly created .CSV file
manbot_df.to_csv(redBlackData)

# if __name__ == '__main__':
#     pass
