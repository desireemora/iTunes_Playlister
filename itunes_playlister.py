from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import os

class track:
    key
    year
    Persistent ID
    Name
    Artist
    Composer
    Album
    Genre
    Location

class playlist:
        songs = []
songs = list()
direc = "/Users/DesireeMora/Music/iTunes/iTunes_Music_Library.xml"

file_name = 'iTunes_Music_Library.xml'
path_to_file = "fill this in"

full_file = os.path.abspath(file_name)
print(full_file)
dom = ElementTree.parse(full_file) # parse an open file

key = dom.findall('dict/dict/dict/')
inte = dom.findall('dict/integer')

count = 1
for k in key:
    print(k.text)

    track = track();
    objs.append()
    if count == 1:
        

    #Every 62 lines is a new song
    if count == 62:
        count = 0

    count+=1
