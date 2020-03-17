Have Python 3.8 installed

edit songBump.py
copy deepbot client API secret found in master settings on deepbot
place API secret in between quotes for deepBotAPISecret
go to pastebin.com/api and log in
go down to 'Your unique developer API key' and copy the key
paste the key in between quotes for pastebinDevKey

save songBump.py


In deep bot, edit these commands

songlist: "Song List: @customapi@[https://localhost:8000/getSongList]"
requestsong: Dont use this. If you can, only allow mods to run it
sr: "!requestSong @target@ @customapi@[https://localhost:8000/addSong]"
songBump: "!requestSong @target@ @customapi@[https://localhost:8000/addPrioritySong]"
internal_songchange_event "@customapi@[https://localhost:8000/getNextSong]"
