from brain import cooktherhythms
from machine import startinsanebot
import os
def startlauncher():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================================")
    print("      PsychBot by nullcode03 (v1.2)     ")
    print("========================================================\n")
    filename = input("[?] which song are u playin? (Enter .json): ").strip() 
    if not os.path.exists(filename):
        print(f"[X] I can't see the file '{filename}' anywhere. make sure its here with me")
        return
    thefinalnotes = cooktherhythms(filename)
    if thefinalnotes:
        print(f"[OK] {len(thefinalnotes)} notes ready for combat.")
        startinsanebot(thefinalnotes, prolag=22)
    else:
        print("[X] that json is emptier than my github.")
if __name__ == "__main__":
    startlauncher()
