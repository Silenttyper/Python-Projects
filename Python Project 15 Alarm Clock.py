from playsound import playsound
import time

playsound("Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3")

CLEAR="-\33[2J"
CLEAR_AND_RETURN="-\33[2H"

def alarm(seconds):
    time_elapsed=0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed+=1
        time_left= seconds  - time_elapsed
        minutes_left=time_left // 60
        seconds_left= time_left % 60

        print(f"Alarm will sound in {CLEAR_AND_RETURN} {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3")

minutes=int*input*"How many minutes to wait"
seconds=int(input("How many seconds to wait"))
total_seconds=minutes * 60 + seconds
alarm(total_seconds)
