import re

# def calibration(calibration_doc):
#     calibration_nr = []
#     written_digits = {"one": '1', 
#                       "two": '2',
#                       "three": '3',
#                       "four": '4',
#                       "five": '5', 
#                       "six": '6', 
#                       "seven": '7', 
#                       "eight": '8', 
#                       "nine": '9'}

#     digits = ["one", '1', 
#                       "two", '2',
#                       "three", '3',
#                       "four", '4',
#                       "five", '5', 
#                       "six", '6', 
#                       "seven", '7', 
#                       "eight", '8', 
#                       "nine", '9']
    
    
#     for s in calibration_doc:
#         for i in range(len(s)):
#             string = s[0:i]
            
            
#             if any(num in string for num in digits):
#                 for key, value in written_digits.items():
#                     new_string = string.replace(key,value)

#                     if new_string != string:
#                         break
#                 m = re.search(r"\d", new_string)

#                 first = m.group()
#                 break

#         for i in range(1,len(s)+1):
#             string = s[-i:]
            
#             if any(num in string for num in digits):
#                 for key, value in written_digits.items():
#                     new_string = string.replace(key,value)

#                     if new_string != string:
#                         break
#                 m = re.search(r"\d", new_string)

#                 last = m.group()
#                 break
#         calibration_nr.append(int(first+last))
      
#     return sum(calibration_nr)

import pandas as pd

def calibration(calibration_doc):
    conversion = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9',
                  "1": '1', "2": '2', "3": '3', "4": '4', "5": '5', "6": '6', "7": '7', "8": '8', "9": '9'}
    
    calibration_nr= []
    for string in calibration_doc:
        matched = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", string)
        all_digits = list(pd.Series(matched).map(conversion))

        calibration_nr.append(int(all_digits[0] + all_digits[-1]))

    return sum(calibration_nr)

    


            

if __name__ == '__main__':
    test = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
            ]
    
    file = open('./advent_of_code/day_1/input.txt', "r")
    calibration_doc = file.readlines()

    print(calibration(test))
