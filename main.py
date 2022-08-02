# Author(s): Eric Mossotti, Colby Ackerman
# About: Red or Black - Gathering data

# Need numpy this time for using weights
import numpy.random
import pandas as pd

# creates placeholder variables to hold random values
blks = 0
reds = 0

# integers signify red = 1, black = 2
possibilities = [1, 2]

# user specifies number of rounds n, red's weight r, and black's weight b
n = int(input("Enter how many rounds n: "))
r = float(input("Enter red's weight: "))
b = float(input("Enter black's weight: "))

# DATA GENERATION STEP
# loop iterates until i equals number of rounds specified by the user

i = 0
while i < n:

    # weights = p, sum of weights are equal to 1
    # returns 1 random value from possibilities
    bots_choice = numpy.random.choice(possibilities, size=1, replace=True, p=[r, b])

    if bots_choice == 1:
        reds = reds + 1

    else:
        blks = blks + 1

    # updates how many turns have passed for the while loop
    i += 1

# creates a dictionary of the randomly generated inputs
bot_dict = {
    '': [''],
    'Reds': [reds],
    'Blacks': [blks]
}

# creates an empty dataframe
bot_df = pd.DataFrame(bot_dict)

# fills in the dataframe in accordance with the dictionary that was created previously
bot_df = bot_df.set_index('')

# test print of the dataframe to confirm that the dataframe was successfully created
print("\n",
      bot_df)

# takes input from user
filepath = str(input("\n"
                     "To create and save a .CSV file of your dataframe\n"
                     "please enter the desired filepath along with the name of the file.\n"
                     "Do not input quotes. Use single backslashes.\n"
                     "e.g.: C:\\folder\\subfolder\\filename.csv"
                     "\n" ))

# creates a file of a user specified path
red_black_data = open(filepath, "x")

# saves the dataframe information to the newly created .CSV file
bot_df.to_csv(red_black_data)


#if __name__ == '__main__':
#    pass
