import numpy as np

if __name__ == "__main__":
    with open('./day_10/test_input.txt', 'r') as f:
        lines = f.readlines()
        loop = []
        for line in lines:
            loop.append([x for x in list(line) if x is not '\n'])
    
        arr = np.array(loop)

    coordinates = np.where(arr == "S")
    og_coordinates = np.array([coordinates[0][0], coordinates[1][0]])
    size = arr.shape

    move = {"|":  np.array([(-1,0), (1,0)]),
            "-":  np.array([(0,1), (0,-1)]),
            "L":  np.array([(-1,0), (0, 1)]),
            "J":  np.array([(-1,0), (0,-1)]),
            "7":  np.array([(1,0), (0,-1)]),
            "F":  np.array([(1,0), (0,1)]),
            ".":  np.array([]),
            "S":  np.array([])
            }

    start = np.array([(0,1), (0,-1), (1,0), (-1,0)])

    max_count = {}
    for x in start:
        count = 0
        current_coordinates = np.array([coordinates[0][0], coordinates[1][0]])
        next_step = x
        while True:
            # print(current_coordinates)
            new_coordinates = np.add(current_coordinates, next_step)
            if 0 <= new_coordinates[0]<= size[0] and 0 <= new_coordinates[1]<= size[1]:
                symbol = arr[new_coordinates[0], new_coordinates[1]]

                if (-next_step).tolist() in move[symbol].tolist():
                    all_moves = move[symbol].tolist()
                    all_moves.remove((-next_step).tolist())
                    count +=1
                    next_step = np.array(all_moves[0])
                    current_coordinates = new_coordinates
                    
                    if f'{current_coordinates}' not in max_count.keys():
                        max_count[f'{current_coordinates}'] = count
                    elif count <= max_count[f'{current_coordinates}']:
                        max_count[f'{current_coordinates}'] = count
                else:
                    break
            else:
                break

    print(max(max_count.values()))
