from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import os

direc = "/Users/DesireeMora/Music/iTunes/iTunes_Music_Library.xml"

file_name = 'iTunes_Music_Library.xml'
full_file = os.path.abspath('/Users/DesireeMora/Music/iTunes/'+file_name)
print(full_file)
dom = ElementTree.parse(full_file) # parse an open file

key = dom.findall('dict/dict/dict/')
inte = dom.findall('dict/integer')
count = 0
for k in key:
    print(k.text)
    #print(k.text,":",inte[count].text)
    count +=1
