'''Игра угадай число'''

import numpy as np

number = np.random.randint(1, 101);

count = 0;
while True:
    count +=1
    predict_number = int(input("Угадай число"));
    
    if predict_number>number:
        print("Число должно быть меньше")
    elif predict_number<number:
        print("Число должно быть больше")
    else: print(f"Угадал за {count} попуток! Это число {number}");