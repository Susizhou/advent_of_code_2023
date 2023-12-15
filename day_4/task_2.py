import re

if __name__ == "__main__":
    cards = {}

    with open('./day_4/input.txt') as f:
        for line in f:
            (key, val) = line.split(':')
            (card_val, my_val) = val.split('|')
            card_nr = re.findall(r'\d+', key)[0]
            cards[int(card_nr)] = {'card_val': card_val.split(' '), 'my_val': my_val[0:-1].split(' ')}

    points = {}
    for card in cards:
        matched = set(cards[card]['my_val']).intersection(set(cards[card]['card_val']))
        if '' in matched:
            matched.remove('')
        
        if card not in points.keys():
            points[card]=1
        else:
            points[card]+=1

        for i in range(card+1,len(matched)+card+1):
            if i not in points.keys():
                points[i]=1*points[card]
            else:
                points[i]+=1*points[card]
        
    

print(sum(points.values()))
