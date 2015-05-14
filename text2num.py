import re

VALUES = {
    'zero':         0,
    'one':          1,
    'two':          2,
    'three':        3,
    'four':         4,
    'five':         5,
    'six':          6,
    'seven':        7,
    'eight':        8,
    'nine':         9,
    'ten':          10,
    'eleven':       11,
    'twelve':       12,
    'thirteen':     13,
    'fourteen':     14,
    'fifteen':      15,
    'sixteen':      16,
    'seventeen':    17,
    'eighteen':     18,
    'nineteen':     19,
    'twenty':       20,
    'thirty':       30,
    'forty':        40,
    'fifty':        50,
    'sixty':        60,
    'seventy':      70,
    'eighty':       80,
    'ninety':       90,
    'hundred':      100,
    'thousand':     1000,
    'million':      1000000,
    'billion':      1000000000,
    'trillion':     1000000000000,
    'quadrillion':  1000000000000000,
    'quintillion':  1000000000000000000,
    'sextillion':   1000000000000000000000,
    'septillion':   1000000000000000000000000,
    'octillion':    1000000000000000000000000000,
    'nonillion':    1000000000000000000000000000000,
    'decillion':    1000000000000000000000000000000000,    
}

def text2num( sentence ):
    target_words = VALUES.keys()
    reg = re.compile('\\b('+'|'.join(target_words)+')\\b', re.IGNORECASE)
    
    # Find all words that describe a number
    matches = []
    for m in reg.finditer(sentence):
        matches.append( [m.group(0), m.start(0), m.end(0)] )

    # If no numbers have been found, return the original sentence
    if (len(matches) == 0):
        return sentence
    
    # Convert words describing numbers into an integer number
    # Algorithm from: https://github.com/ghewgill/text2num/blob/master/text2num.py
    total = 0
    sum_value = 0
    for m in matches:
        v = VALUES.get(m[0].lower(), None)
        if v < 100:
            sum_value += v
        elif v == 100: # Special case
            sum_value *= 100
        else:
            total += sum_value * v
            sum_value = 0
    total += sum_value
    
    start_idx = [i[1] for i in matches]
    end_idx = [i[2] for i in matches]
    return sentence[:min(start_idx)] + str(total) + sentence[max(end_idx):]