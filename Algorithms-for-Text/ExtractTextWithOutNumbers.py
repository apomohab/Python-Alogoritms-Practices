# in 19 - 9 - 2022 .

import re

def ExtractText():

    TheText = "im lean Python in 2022 - i have 3000 students"

    Extract = re.sub(r'[^a-zA-Z]' , "" , TheText)

    print(Extract)

ExtractText()

