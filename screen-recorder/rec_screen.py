import cv2          #pip install opencv-python
import numpy
import pyautogui    #pip install PyAutoGUI
import keyboard     #pip install keyboard
from datetime import date, time
import tkinter as tk #pip install tk

#get screen infos of current using screen 
root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#get todays date 
today = date.today().strftime("%d.%m.%Y")           #todays date with given format


#create screenrecorder 
filename = f"{today}_record"                        #name of the file
screen_size = (screen_width, screen_height)         #screen screensize
codec = cv2.VideoWriter_fourcc(*'mp4v')             #format 
vid = cv2.VideoWriter(filename + '.mp4', codec, 20.0 , ( screen_size))                             #containers: with filename + fileending, codec, fpsnumber, screensize

print ('start recording')
while True:
    img = pyautogui.screenshot()
    numpy_frame = numpy.array(img)
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
    vid.write(frame)

    if keyboard.is_pressed('^'):        #button to stop recording
    
        print ('end recording')
        break 

cv2.destroyAllWindows()
vid.release()