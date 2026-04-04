import time
import keyboard
import pydirectinput
pydirectinput.PAUSE = 0
GAMERBUTTONS = {0: 'left', 1: 'down', 2: 'up', 3: 'right'}
def startinsanebot(notezz, prolag=22, extrahold=45):
    print("\n[!] bot is warming up...")
    print("[>] press f1 when receptor hits arrowbar")
    keyboard.wait('f1') # waits for F1 key to be pressed, make sure u get ur timing right cuz this aint automatic
    momentoftruth = time.time() * 1000
    pointer = 0
    stuckkeys = {} 
    print("[+] bot playin. Press esc to kill")
    while pointer < len(notezz) or stuckkeys:
        if keyboard.is_pressed('esc'): 
            print("\n[!] aborting mission...")
            break
			
        currentflighttime = (time.time() * 1000) - momentoftruth
        if pointer < len(notezz):
            currentnote = notezz[pointer]
            if currentflighttime >= (currentnote['ms'] - prolag):
                keytopress = GAMERBUTTONS[currentnote['finger']]
                pydirectinput.keyDown(keytopress)
                releasetime = (currentnote['end'] + extrahold) if currentnote['isstretch'] else (currentnote['ms'] + 25)
                stuckkeys[currentnote['finger']] = releasetime
                pointer += 1
        for k in list(stuckkeys.keys()):
            if currentflighttime >= stuckkeys[k]:
                pydirectinput.keyUp(GAMERBUTTONS[k])
                del stuckkeys[k]
