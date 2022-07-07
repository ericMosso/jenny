from os import stat
from random import choice
from utility import clamp
from table import Table

stats = Table('Red or Black', [
    'guess',
    'correct'
])

options = ['red', 'black']

rounds = clamp(
    int(input('How many times? ')), 
    0,          # min
    1_000_000   # max
)

for _ in range(rounds):
    chosen = choice(options)
    guess = choice(options)
    correct = guess == chosen
    stats.addRow(guess, correct)

print(stats)
stats.export('redorblack.csv', append=False)
stats.export('redorblackAppend.csv')