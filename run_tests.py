import unittest
from text2num import text2num

class TestCase(unittest.TestCase):
        
    def test_function(self):
        str_in = "I have eighty one apples."
        str_out = text2num(str_in)
        assert(str_out == "I have 81 apples.")
    
        str_in = "TWO HUNDRED THOUSAND DOLLARS IS WHAT YOU OWE ME!"
        str_out = text2num(str_in)
        assert(str_out == "200000 DOLLARS IS WHAT YOU OWE ME!")
        
        str_in = "Nothing to see here"
        str_out = text2num(str_in)
        assert(str_out == "Nothing to see here")        
    
        str_in = "There are six billion five hundred fifty four million nine hundred eleven thousand three hundred twenty one people."
        str_out = text2num(str_in)
        assert(str_out == "There are 6554911321 people.")       
        
if __name__ == '__main__':
    unittest.main()        