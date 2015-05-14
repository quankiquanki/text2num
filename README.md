text2num
===============

This is a function that converts textual numbers in a string to their integer representation. A handy function for applications that deal with Natural Language Processing (NLP).

Example
===============

    from text2num import text2num
    
    in_string = "I have seventeen cars, three hundred twenty seven servants, five thousand houses and two million and twenty three hundred dollars."
    out_string = text2num(in_string)
    print out_string
    
    Output:
    I have 17 cars, 327 servants, 5000 houses and 2002300 dollars.

Things to Note
===============
- It can handle multiple textual numbers in an input string.
- It assumes the input string is in english and that it is correctly written. So no oddly described numbers like "one million thousand two hundred billion million five"

LICENSE
===============
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).