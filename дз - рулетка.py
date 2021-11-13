import numpy as np
import random
#import matplotlib.pyplot as pit
#import matplotlib.mlab as mlab

np.random.randint(0, 36)
#1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23,25, 27, 30, 32, 34, 36 = 'red'
#2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35 = 'black'
#0 = 'green'
case = {0 :'green', 1 : 'red', 2 :'black' , 3:'red' , 4:'black' , 5:'red' , 6:'black' , 7 : 'red' , 8: 'black', 9 : 'red', 10 :'black' , 11 :'black', 12 : 'red',
 13 :'black', 14 :'red', 15 :'black' , 16 :'red', 17: 'black', 18 : 'red', 19: 'red', 20:'black', 21: 'red', 22 :'black' , 23: 'red', 24:'black', 25: 'red', 26:'black' , 27: 'red', 28: 'black', 29:'black', 30:'red', 31: 'black', 32: 'red', 34: 'red', 35:'black', 36:'red'}
for i in range(0, 3):
    a = int(input("Get play the game!\n Enter a number from 0 to 36: "))
    x = np.random.randint(0, 36)
    if x == a:
        print(f'You win! {x}, {case.get(x)} ')
    else:
        print(f' {x} - {case.get(x)} wins. You lose!')