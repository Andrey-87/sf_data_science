#Игра угадай число
import numpy as np
number = np.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input("Please input a number from 1 to 100"))
    if predict_number > number:
        print('number should be less')
    elif predict_number < number:
        print('number should be more')
    else:
        print(f"BINGO! it is {number} after {count} tries")
        break
    