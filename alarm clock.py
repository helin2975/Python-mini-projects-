
import time # ! To update the clock every second
import datetime # ! To work with string representations of a time 
import pygame # ! To work with sound effects (there are many alternatives)


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\ketan\Downloads\That's That (Sting) - Twin Musicom.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Wake UP😣😣")
            pygame.mixer.init() # ! mixer is a module for loading and playing sound  and the init is the initialize method (another way to call a constructor) and we can pass different arguments like frequency,size,buffer etc (use the default settings)
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play() #! This will play until the program terminates 
            
            while pygame.mixer.music.get_busy(): # ! This will help us to play the music until the music is over or we forcefully terminates the program 
                # ! The get_busy method will return boolean value 
                time.sleep(1)
                
            is_running =False
            
            
        time.sleep(1) # ! This will update the time every second because when the loop runs it will print the current time with delay of 1 sec         
        
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS):")
    set_alarm(alarm_time)
    