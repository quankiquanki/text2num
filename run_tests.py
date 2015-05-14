import unittest
from text2num import text2num

class TestCase(unittest.TestCase):
        
    def test_function(self):
        str_in = "No numbers in this sentence."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)
        assert(str_out == "No numbers in this sentence.") 
                
        str_in = "I have eighty one apples."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)
        assert(str_out == "I have 81 apples.")
    
        str_in = "TWO HUNDRED THOUSAND DOLLARS IS WHAT YOU OWE ME!"
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "200000 DOLLARS IS WHAT YOU OWE ME!")
        
        str_in = "The number here is ten thousand three hundred forty one"
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "The number here is 10341")        
    
        str_in = "There are six billion and five hundred fifty four million and nine hundred eleven thousand and three hundred twenty one people."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "There are 6554911321 people.")
        
        str_in = "Kenneth will get twenty two hundred apples while Keith gets sixty seven."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "Kenneth will get 2200 apples while Keith gets 67.")
        
        str_in = "I have seventeen cars, three hundred twenty seven servants, five thousand houses and two million and twenty three hundred dollars."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "I have 17 cars, 327 servants, 5000 houses and 2002300 dollars.")        
        
        str_in = "Two hundred and eighty two melons are laying in that box."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "282 melons are laying in that box.")
        
        str_in = "This is a hundred hundred and a thousand thousand."
        str_out = text2num(str_in)
        print 'Input:\t%s\nOutput:\t%s\n' % (str_in, str_out)      
        assert(str_out == "This is a 100 100 and a 1000 1000.")                      
        
if __name__ == '__main__':
    unittest.main()        