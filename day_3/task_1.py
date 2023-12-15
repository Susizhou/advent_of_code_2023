import numpy as np

def sum_engine_number():
    return None


if __name__ == '__main__':
    data =[]
    with open('./advent_of_code/day_3/input.txt') as f:
        for line in f:
            data.append(list(line)[0:-1])

    #print(data)    
    array = np.array(data, dtype=str)
    print(array)

