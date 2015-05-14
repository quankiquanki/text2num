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
    groups = []
    for m in reg.finditer(sentence):
        new_number = True        
        for g in groups:
            if (m.start(0) - g[2] <= 1 or sentence[g[2]:m.start(0)].lower() == ' and ') and m.group(0) != g[0][-1]:
                g[0].append( m.group(0) )
                g[2] = m.end(0)
                new_number = False
                
        if new_number:
            new_number = False
            groups.append( [ [m.group(0)], m.start(0), m.end(0) ] )

    # If no numbers have been found, return the original sentence
    if (len(groups) == 0):
        return sentence
    
    # Convert words describing numbers into an integer number
    # Algorithm from: https://github.com/ghewgill/text2num/blob/master/text2num.py
    for g in groups:
        total = 0
        sum_value = 0  
        for m in g[0]:
            v = VALUES.get(m.lower(), None)
            if v < 100:
                sum_value += v
            
            # Special case for independent magnitudes
            elif sum_value == 0:
                sum_value = v
                continue
            
            # Special case
            elif v == 100:
                sum_value *= 100
                
            else:
                total += sum_value * v
                sum_value = 0
        total += sum_value
        g.append( total )
    
    # Construct the new sentence
    sentence_parts = []
    s_start = 0
    for g in groups:
        g_start = g[1]
        g_end = g[2]
        
        sentence_parts.append(sentence[s_start:g_start])
        sentence_parts.append( str(g[3]) )
        s_start = g_end
    sentence_parts.append( sentence[s_start:] )
    
    return ''.join(sentence_parts)