#Q: http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
import re

def get_challenge(subject):
    text_src=urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % subject).read()
    return text_src

# text=get_challenge('12345')
# and the next_str nothing is 16044
# Yes. Divide by two and keep going.
# text=get_challenge('8022')
# There maybe misleading numbers in the 
# text. One example is 82683. Look only for the next_str nothing and the next_str nothing is 63579
text=get_challenge('63579')
next_str=re.compile('and the next_str nothing is ([0-9]+)').match(text).groups()[0]
print next_str
while next_str:
    text=get_challenge(next_str)
    print text
    next_str=re.compile('and the next_str nothing is ([0-9]+)').match(text).groups()[0]

# peak.html
# Level 5: http://www.pythonchallenge.com/pc/def/peak.html
