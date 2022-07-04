# Author(s): Eric Mossotti, Colby Ackerman
# About: Red or Black - Gathering data
from random import choice
import pandas as pd

blkBot = 0
redBot = 0

blkMan = 0
redMan = 0

possibilities = ['red', 'black']

n = int(input("Enter how many rounds n: "))

i = 0
while i < n:
    # bot choice using random data generator aka jenny
    botsChoice = choice(possibilities)
    if botsChoice == 'red':
        redBot = redBot + 1
    else:
        blkBot = blkBot + 1

    x = input("Red or black?: ")
    if x == 'red':
        redMan = redMan + 1
    else:
        blkMan = blkMan + 1

    i = i + 1

manbot_dict = {'Man|Bot': ['Bot', 'Man'], 'Reds': [redBot, redMan], 'Blacks': [blkBot, blkMan]}
manbot_df = pd.DataFrame(manbot_dict)
manbot_df = manbot_df.set_index('Man|Bot')

print(manbot_df)




# if __name__ == '__main__':
#     pass
