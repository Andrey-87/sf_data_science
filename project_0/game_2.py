### Игра угадай число. Программа сама угадывает ###
import numpy as np

def number_predict(number:int=1) -> int:
    """программа угадывает число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if predict_number == number:
            break
    return count

print(f'Кол-во попыток {number_predict(10)}')

def score_game(number_predict) -> int:
    """averrage amount of attampts

    Args:
        number_predict (int): функция угадывания

    Returns:
        int: кол-во попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101,size=(1000))
    for number in random_array:
        count_ls.append(number_predict(number))
    score = int(np.mean(count_ls))
    print(f'ваш алгоритм укадывает в среднем за {score} попыток')
    return score

#run

if __name__ == '__main__':
    score_game(number_predict)
    