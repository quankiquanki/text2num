import re

def words_to_number( sentence ):
    
    # Search for these numberwords
    expression = ('\\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|'
                'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
                'eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|'
                'eighty|ninety|hundred|thousand|million|billion)\\b')
    # Values of the words found in the expression
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
    20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000]
    
    reg = re.compile(expression, re.IGNORECASE)
    
    # Find all numberwords in the sentence and save the location.				
    matches = []
    start_idx = -1
    end_idx = -1
    for m in reg.finditer(sentence):
        if (start_idx == -1):
            start_idx = m.start(0)
        end_idx = m.end(0)
        matches.append(m.group(0))
    
    # If no numberwords have been found, return the sentence
    if (start_idx == -1):
        return sentence
    # Assign values to the found words
    words = expression[3:-3].split("|")
    for idxw, w in enumerate(matches):
        w = w.lower()
        for idxv, v in enumerate(words):
            if (w == v):
                matches[idxw] = values[idxv]
                break
    # Add and Multiply the values to create the total number using these steps
    # 1) If the last value is smaller than the current one -> Multiply
    # 2) If the last value is bigger -> Add
    # 3) If a Multiply has been performed and there is another Multiply, add the value
    #	from the last multiplication to variable total and start over from the last
    #	multiplication.
    sum = -1
    last_value = -1
    last_midx = -1
    last_msum = -1
    last_mvalue = -1
    total = 0
    i = 0
    while (i != len(matches)):
        if (last_value == -1):
            last_value = matches[i]
            sum = last_value
            i += 1
            continue
        
        if (last_value < matches[i]):
            if (matches[i] < last_mvalue):
                i = last_midx+1
                total += last_msum
                lastValue = last_mvalue
                sum = 0
                
                last_midx = -1
                last_msum = -1
                last_mvalue = -1
                continue
            sum *= matches[i]
            
            last_midx = i
            last_msum = sum
            last_mvalue = matches[i]
        else:
            sum += matches[i]
        last_value = matches[i]
        i += 1
    total += sum
    return sentence[:start_idx] + str(total) + sentence[end_idx:]	