from random import randint 
from random import shuffle

mastermind = [m.upper() for m in 'mastermind']
mastermind_shuffled = mastermind.copy()
while True:
    try:
        shuffle(mastermind_shuffled)
        print(''.join(mastermind_shuffled))
    except KeyboardInterrupt:
        print (''.join(mastermind))
        # If you actually want the program to exit
        raise