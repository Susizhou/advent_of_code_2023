import re

if __name__ == "__main__":
    cards = {}

    with open('./day_4/input.txt') as f:
        for line in f:
            (key, val) = line.split(':')
            (card_val, my_val) = val.split('|')
            card_nr = re.findall(r'\d+', key)[0]
            cards[int(card_nr)] = {'card_val': card_val.split(' '), 'my_val': my_val[0:-1].split(' ')}

    points = 0
    for card in cards:
        matched = set(cards[card]['my_val']).intersection(set(cards[card]['card_val']))
        if '' in matched:
            matched.remove('')

        if len(matched) == 0:
            points += 0
        else:
            card_point = 2**(len(matched)-1)
            points+=card_point
    
    print(points)
