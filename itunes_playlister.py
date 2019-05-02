from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import os

class tracks:
    key = 0
    year = 0
    persistent_ID = "None"
    name= "None"
    artist= "None"
    composer= "None"
    album= "None"
    genre= "None"
    location= "None"

class playlist:
        songs = []
        
songs = {}
direc = "/Users/DesireeMora/Music/iTunes/iTunes_Music_Library.xml"

file_name = 'iTunes_Music_Library.xml'
path_to_file = "fill this in"

full_file = os.path.abspath(file_name)
print(full_file)
dom = ElementTree.parse(full_file) # parse an open file

key = dom.findall('dict/dict/dict/')
inte = dom.findall('dict/integer')

count = 1
total_songs = 0

track = tracks()

for k in key:
    #print(k.text)
    
    #Track ID/Key
    if count == 2:
        track.key = k.text
    #Year
    if count == 16:
        track.year = k.text
    #Persistant ID
    if count == 28:
        track.persistent_ID = k.text
    #Name
    if count == 42:
        track.name = k.text
    #Artist
    if count == 44:
        track.artist = k.text
    #Composer
    if count == 48:
        track.composer = k.text
    #Album
    if count == 50:
        track.album = k.text
    #Genre
    if count == 52:
        track.genre = k.text
    #Location
    if count == 62:
        track.location = k.text
        

    #Every 62 lines is a new song
    if count == 62:
        count = 0
        total_songs = total_songs + 1
        #print(track.key)
        songs[track.key]= track
        #print(total_songs)
        
        

    count+=1
    print(count)
