import re

def words_to_number( sentence ):
    
    values = [  (0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'),
                (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'),
                (8, 'eight'), (9, 'nine'), (10, 'ten'), (11, 'eleven'),
                (12, 'twelve'), (13, 'thirteen'), (14, 'fourteen'), (15, 'fifteen'),
                (16, 'sixteen'), (17, 'seventeen'), (18, 'eighteen'), (19, 'nineteen'),
                (20, 'twenty'), (30, 'thirty'), (40, 'forty'), (50, 'fifty'),
                (60, 'sixty'), (70, 'seventy'), (80, 'eighty'), (90, 'ninety'),
                (100, 'hundred'), (1000, 'thousand'), (1000000, 'million'), (1000000000, 'billion')
            ]
    reg = re.compile('\\b('+'|'.join([i[1] for i in values])+')\\b', re.IGNORECASE)
    
    # Find all numberwords in the sentence and save the location.				
    matches = []
    start_idx = -1
    end_idx = -1
    for m in reg.finditer(sentence):
        if (start_idx == -1):
            start_idx = m.start(0)
        end_idx = m.end(0)
        matches.append( [m.group(0), m.start(0), m.end(0)] )
    
    # If no numberwords have been found, return the sentence
    if (len(matches) == 0):
        return sentence
        
    # Assign values to the found words
    for i in range(0, len(matches)):
        w = matches[i][0].lower()
        for v in values:
            if (w == v[1]):
                matches[i].append(v[0])
                break
    word_values = [i[3] for i in matches]
                    
    # Add and Multiply the values to create the total number using these steps
    # 1) If the last value is smaller than the current one -> Multiply
    # 2) If the last value is bigger -> Add
    # 3) If a Multiply has been performed and there is another Multiply, add the value
    #	from the last multiplication to variable total and start over from the last
    #	multiplication.
    last_midx = -1
    last_msum = -1
    last_mvalue = -1
    total = 0

    last_value = word_values[0]   
    sum = last_value    
    i = 1
    while i != len(word_values):
        if (last_value < word_values[i]):
            if (word_values[i] < last_mvalue):
                i = last_midx+1
                total += last_msum
                lastValue = last_mvalue
                sum = 0
                
                last_midx = -1
                last_msum = -1
                last_mvalue = -1
                continue
            sum *= word_values[i]
            
            last_midx = i
            last_msum = sum
            last_mvalue = word_values[i]
        else:
            sum += word_values[i]
        last_value = word_values[i]
        i += 1
    total += sum
    
    return sentence[:start_idx] + str(total) + sentence[end_idx:]	