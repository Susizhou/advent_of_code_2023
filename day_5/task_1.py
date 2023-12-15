import pandas as pd

def mapping_2(dataframe, maps):
    if len(maps) == 0:
        location = dataframe[dataframe.columns[-1]]
        print(min(location))
        return (min(location))

    count = 0
    new_column = []
    for element in dataframe[dataframe.columns[-1]]:
        count +=1
        for map_3 in maps[0]:
            [destination, source, range_len] = map_3.split(" ")

            if element in range(int(source), int(source) + int(range_len)):
                new_column.append(element-int(source)+int(destination))
        if len(new_column) != count:
            new_column.append(element)

    number = len(dataframe.columns)-1
    dataframe[f"{number}"] = new_column
    maps.pop(0)

    mapping_2(dataframe, maps) 

if __name__ == "__main__":
    with open('./day_5/test_input.txt') as f:
        file =f.read()

        variables = [i.split('\n') for i in file.split('\n\n') if i]

    seeds = variables[0][0].split(": ")[1:][0]
    dataframe = pd.DataFrame([int(i) for i in seeds.split(" ")])

    maps = variables[1:]

    maps_list = []
    for map_element in maps:
        maps_list.append(map_element[1:])

    mapping_2(dataframe, maps_list)
