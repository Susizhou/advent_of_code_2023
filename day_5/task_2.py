import pandas as pd

def mapping_2(pairs, maps_df):
    new_ranges = []
    for pair in pairs:
        for sets in maps_df.iloc[0].dropna().iloc[1:]:
            [destination, source, range_len] = sets.split(" ")
            if int(source) <pair[0]< int(source) + int(range_len):



if __name__ == "__main__":
    with open('./day_5/input.txt') as f:
        file =f.read()
        variables = [i.split('\n') for i in file.split('\n\n') if i]

    seeds = [int(i) for i in variables[0][0].split(": ")[1:][0].split(" ")]
    pairs = tuple(zip(seeds[0::2],seeds[1::2]))

    maps = variables[1:]
    maps_df = pd.DataFrame(maps)

    mapping_2(pairs,maps_df)

            
