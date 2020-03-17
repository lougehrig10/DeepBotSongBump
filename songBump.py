import websocket
import json
from pastebin import PastebinAPI
from http.server import HTTPServer, BaseHTTPRequestHandler


deepBotAPISecret = ""
pastebinDevKey = ""




class APIManager(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == "/addPrioritySong":
            addPrioritySong()
        elif self.path == "/addSong":
            addSong()
        elif self.path == "/getNextSong":
            sendNextSong()
        elif self.path == "/getSongList":
            self.wfile.write(getSongList().encode("utf8"))

def sendNextSong():
    if not prioritySongList.empty():
        runCommand("requestSong " + prioritySongList.pop(0)[0])
    elif not songList.empty():
        runCommand("requestSong " + songList.pop(0)[0])

def runCommand(command):
    ws.send("api|run_command|" + command)

def addPrioritySong():
    prioritySongList.append(pullRequestedSong())

def addSong():
    songList.append(pullRequestedSong())

def pullRequestedSong():
    ws.send("api|get_songs|2|1")
    song = json.loads(ws.recv())["msg"][0]
    return [song["songID"],song["songName"]]

def getSongList():

    text = ""

    for song in iter(prioritySongList.get,None):
        text += song[1]
    for song in iter(songList.get,None):
        text += song[1]

    return PastebinAPI.paste(pastebinDevKey,text,paste_private = 'unlisted', paste_expire_date = '10M')

def runHTTPServer():
    server_address = ("localhost",8000)
    httpd = HTTPServer(server_address, APIManager)

    httpd.serve_forever()








prioritySongList = []
songList = []

ws = websocket.WebSocket()
ws.connect("ws://localhost:3337")
ws.send("api|register|" + deepBotAPISecret)

runHTTPServer()
