# level (6): http://www.pythonchallenge.com/pc/def/channel.html
# Get http://www.pythonchallenge.com/pc/def/channel.zip
# In readme.txt
# 
# hint1: start from 90052 --> Next nothing is 94191
# hint2: answer is inside the zip

import urllib
import zipfile
import re

def get_file():
    urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip','D:\\channel.zip')
  
get_file()
zip_file=zipfile.ZipFile('D:\\channel.zip')

file_list=[]
next_str='90052'
file_content=zip_file.read('%s.txt' % next_str)
while next_str:
    file_list.append("%s.txt" % next_str)
    next_str=re.compile('Next nothing is ([0-9]+)').match(file_content)
    if next_str:
        next_str=next_str.groups()[0]
        file_content=zip_file.read('%s.txt' % next_str)
        print file_content
    else:
        break
    
# print: Collect the comments.
print "".join([zip_file.getinfo(i).comment for i in file_list])

#Next level (7): http://www.pythonchallenge.com/pc/def/hockey.html
# it's in the air. look at the letters.
# So the real level 7 is http://www.pythonchallenge.com/pc/def/oxygen.html