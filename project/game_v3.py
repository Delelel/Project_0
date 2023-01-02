'''Комп угадай число'''

import numpy as np

def random_predict_number(number:int=1) -> int:
    """Комп рандомно угадывает число

    Args:
        number (int, optional): Загадываемое число. Defaults to 1.

    Returns:
        int: Кол-во попыток
    """

    count = 0;
    limiter_low = 1
    limiter_hight = 100
    while True:
        count +=1
        predict_number = np.random.randint(limiter_low,limiter_hight+1);
        
        if predict_number == number:
            break;
        elif predict_number < number:
            limiter_low = predict_number
        elif predict_number > number:
            limiter_hight = predict_number
    
    return count;


def score_game(random_predict_number) -> int:
    """Сколько в среднем угадывает

    Args:
        random_predict_number (func): Функция угадываения числа компом

    Returns:
        int: Среднее кол-во попыток
    """
    
    count_ls = [];
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict_number(number))
    
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    
    return score;

if __name__ == "__main__":
    score_game(random_predict_number)