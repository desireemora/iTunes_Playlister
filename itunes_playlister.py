from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import os

class tracks:
    key = 0
    year = 0
    #persistent ID
    pid = "None"
    name= "None"
    artist= "None"
    composer= "None"
    album= "None"
    genre= "None"
    location= "None"

class playlist:
        songs = []

dic_of_songs = {}
direc = "/Users/DesireeMora/Music/iTunes/iTunes_Music_Library.xml"

file_name = 'iTunes_Music_Library.xml'
path_to_file = "fill this in"

full_file = os.path.abspath(file_name)
print(full_file)
dom = ElementTree.parse(full_file) # parse an open file

key = dom.findall('dict/dict/dict/')
inte = dom.findall('dict/integer')

count = 0
total_songs = 0

track = tracks()

for index,k in enumerate(key):
    count+=1

    #Track ID/Key
    if k.text == "Track ID":
        cur_key = key[index+1].text
        print("Track ID: ",cur_key)

    #Year
    if k.text == "Year":
        cur_year = key[index+1].text
        print("Year: ",cur_year)

    #Persistent ID
    if k.text == "Persistent ID":
        cur_pid = key[index+1].text
        print("Persistent ID: ",cur_pid)

    #Song Name
    if k.text == "Name":
        cur_name = key[index+1].text
        print("Name: ",cur_name)

    #Artist Name
    if k.text == "Artist":
        cur_artist = key[index+1].text
        print("Artist: ",cur_artist)

    #composer(s) Name
    if k.text == "Composer":
        cur_composer = key[index+1].text
        print("Composer: ",cur_composer)

    #Album Name
    if k.text == "Album":
        cur_album = key[index+1].text
        print("Album: ",cur_album)

    #Genre
    if k.text == "Genre":
        cur_genre = key[index+1].text
        print("Genre: ",cur_genre)

    #Location (File Path)
    if k.text == "Location":
        cur_location = key[index+1].text
        print("Location: ",cur_location)

    #Makes sure that I dont access an index that does not exist
    #if len(key) <= index:
    if key[index+1].text == "Track ID":
        
        dic_of_songs[cur_key] = tracks()
        dic_of_songs[cur_key].key = cur_key
        dic_of_songs[cur_key].year = cur_year
        dic_of_songs[cur_key].pid = cur_pid
        dic_of_songs[cur_key].name = cur_name
        dic_of_songs[cur_key].artist = cur_artist
        dic_of_songs[cur_key].composer = cur_composer
        dic_of_songs[cur_key].album = cur_album
        dic_of_songs[cur_key].genre = cur_genre
        dic_of_songs[cur_key].location = cur_location

        print("Object Key & Year: ",dic_of_songs[cur_key].key," ",dic_of_songs[cur_key].name)

        print()
        print("*****************NEW TRACK****************")
        
