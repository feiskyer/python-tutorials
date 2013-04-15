# http://www.pythonchallenge.com/pc/def/oxygen.html
import urllib
import Image    # requires Python Imaging Library (PIL)

urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png','D:\\oxygen.png')
img=Image.open('D:\\oxygen.png')
w,h=img.size
pixs = [img.getpixel((x, h/2)) for x in range(0, w, 7)]
rr=[r for r, g, b, a in pixs if r == g == b]
print "".join(map(chr,rr))
#print: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

print "".join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))
# print integrity

# Next level (8) http://www.pythonchallenge.com/pc/def/integrity.html