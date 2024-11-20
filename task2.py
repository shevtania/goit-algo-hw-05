import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\s\d+\.?\d*\s" # pattern for number with spices on the sides
    for word in re.finditer(pattern, text): # iterable finding word
        num = float(word.group().strip()) # cut spaces and turn into float
        yield num
    
     
def sum_profit(text: str, func: Callable):
# sum numbers from generator    
    return sum(func(text))

#text = 'dfhwiefh  12 fwh 4.7 eofhi 14 lkdf 0.6 hwofh 64543 lefh 453.9787 n'
text = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
print(sum_profit(text, generator_numbers))

