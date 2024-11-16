import re
from typing import Callable

def generator_numbers(text: str):
    for word in text.split():  # loop in list after spliting text
        if re.search(r"\d+\.*\d+", word):  # find float number
            yield float(word)
    
def sum_profit(text: str, func: Callable):
# sum numbers from generator    
    return sum(func(text))

text = 'dfhwiefh  12 fwh 4.7 eofhi 14 lkdf 0.6 hwofh 64543 lefh 453.9787 n'
print(sum_profit(text, generator_numbers))
