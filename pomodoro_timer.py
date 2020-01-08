import time 
import math
import sys
import os 


def start_timer(duration):
    i = duration * 60
    while i > 0:
        i -= 1
        minutes = math.floor(i / 60)
        seconds =  int(i % 60)
        minutes, seconds = str(minutes), str(seconds)
        
        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(seconds) == 1:
            seconds = "0" + seconds

        print(f"{minutes}:{seconds}")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

    print("...Timer Stopped")
    restart_timer()
    
    
def restart_timer():
    choice = input("Start Again? [y/n]: ")
    if choice == "y":
        start_timer(duration)
    elif choice == "n":
        sys.exit()


if __name__ == "__main__":
    print(r"""
  _____   ____  __  __  ____  _____   ____  _____   ____  
 |  __ \ / __ \|  \/  |/ __ \|  __ \ / __ \|  __ \ / __ \ 
 | |__) | |  | | \  / | |  | | |  | | |  | | |__) | |  | |
 |  ___/| |  | | |\/| | |  | | |  | | |  | |  _  /| |  | |
 | |    | |__| | |  | | |__| | |__| | |__| | | \ \| |__| |
 |_|_____\____/|_|  |_|\____/|_____/ \____/|_|  \_\\____/ 
 |__   __|_   _|  \/  |  ____|  __ \                      
    | |    | | | \  / | |__  | |__) |                     
    | |    | | | |\/| |  __| |  _  /                      
    | |   _| |_| |  | | |____| | \ \                      
    |_|  |_____|_|  |_|______|_|  \_\                     
                                                          
                                                          """)
    duration = float(input("How Long? (minutes): "))
    start_timer(duration)

    
    
   