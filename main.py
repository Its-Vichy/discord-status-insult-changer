from colorfull import init; init()
import websocket
import threading
import httpx
import json
import time

def init_websocket(token: str):
    ws = websocket.WebSocket()
    ws.connect(url= 'wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream')
    ws.send(json.dumps({"op":2,"d":{"token": token,"capabilities":125,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"fr","browser_user_agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0","browser_version":"95.0","os_version":"","referrer":"https://discord.com/","referring_domain":"discord.com","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":107767,"client_event_source":None},"presence":{"status":"online","since":0,"activities":[],"afk":False},"compress":False,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}))
    
    print(f'[+] Connected to websocket | {token}')
    return ws

def status_changer(ws: websocket.WebSocket):
    while True:
        insult = httpx.get('https://insult.mattbas.org/api/insult.txt').text
        print(f'[+] {insult}.')
        
        ws.send(json.dumps({"op":3,"d":{"status":"online","since":0,"activities":[{"name":"Custom Status","type":4,"state": insult,"emoji":{"id":None,"name":"ð","animated":False}}],"afk":False}}))
        time.sleep(5)

for token in open('./tokens.txt', 'r+').read().splitlines():
    threading.Thread(target=status_changer, args=(init_websocket(token),)).start()
