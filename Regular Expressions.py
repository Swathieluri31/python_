#Meta-characters
#[] - represent a set of characters
#\ - refer to a special character
#. - represents any special character
#^ - matches the start of a string
#\$ - matches the end of a string
#* - matches zero or more occurrences of the preceding character

import re
p = re.compile('/d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
p = re.compile(r'\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# 
import re
def findMonthAndDate(string):

    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
    if match == None:
        print ("Not a valid date")
        return
    print ("Given Data: %s" % match.group())
    print ("Month: %s" % match.group(1))
    print ("Date: %s" % match.group(2))

# Driver code
findMonthAndDate("June 24")
print("")
findMonthAndDate("I was born on June 24")

#
import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")

if match is not None:
    print(f"Match at index {match.start()}, {match.end()}")
    print(f"Full match: {match.group(0)}")
    print(f"Month: {match.group(1)}")
    print(f"Date: {match.group(2)}")
else:
    print("The regex pattern does not match.")

#
