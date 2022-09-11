# on - 10 - 9 - 2022 .
# how to count words in text used pyton ..
# saeed.cooder@gmail.com
# twitter @Saeed_Coder

import collections

def Word_Counts():

    The_Text = """

    However, the number of occurrences of this operator must be equal to the number of strings to replace with after the % sign.
    Otherwise, an error of the type “TypeError: not enough arguments for format string” is thrown.

    However, the number of occurrences of this operator must be equal to the number of strings to replace with after the % sign. 
    Otherwise, an error of the type “TypeError: not enough arguments for format string” is thrown.
    
    
    """

    words = The_Text.split()
    words_count = collections.Counter(words)

    for word , count in sorted(words_count.items()):

        if count > 1 :

            print(f" This word  - {word} Count is {count}")

        else :

            print("Thos Word not find")

Word_Counts()
