import tkinter as tk
from tkinter import *
from tkinter import ttk

import pygame 
from pygame import mixer

import time
import os
import random 

mixer.init()

root = tk.Tk() 
root.title('Mp3 Player')
root.geometry('350x400')

canvas = tk.Canvas(root, bg="gray55")
canvas.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.80, relheight=0.80, relx=0.1, rely=0.1)

picture = PhotoImage(file = "image_files/music_notes_PNG75.png") 
pictureCanvas = Label(frame, image=picture) 
pictureCanvas.place(relwidth=0.50, relheight=0.50, relx=0.23, rely=0.15)  

#Global variable for play/pause button looping
buttonCounter = 0
playlist = ["mp3_files/song1.mp3","mp3_files/song2.mp3","mp3_files/song3.mp3"] 
song = 0

#Play button group
playImage = PhotoImage(file='image_files/play.png') 

def playAudio():
    global buttonCounter, song, playlist
    if buttonCounter == 0:  
        mixer.music.load(playlist[song])
        mixer.music.play()
        buttonCounter += 2
        playNext() 
    elif buttonCounter == 1:
        mixer.music.unpause()
        buttonCounter += 1 
    
playButton = Button(frame, image=playImage, command = playAudio, highlightthickness = 0)
playButton.place(relwidth=.25, relheight=0.10, relx=.25, rely=.9)

#Pause button group
pauseImage = PhotoImage(file='image_files/music-player.png')  

def pauseAudio():
    global buttonCounter
    if buttonCounter == 2:
        mixer.music.pause()
        buttonCounter -= 1
            
pauseButton = Button(frame, image=pauseImage, command = pauseAudio, highlightthickness = 0)
pauseButton.place(relwidth=.25, relheight=0.10, relx=.5, rely=.9)

#Skip button group  
skipImage = PhotoImage(file='image_files/next.png')

def skipAudio():
    global buttonCounter, song
    buttonCounter *= 0
    song += 1
    if(song == len(playlist)):
        song = 0 
    playAudio()  

skipButton = Button(frame, image=skipImage, command = skipAudio, highlightthickness = 0)
skipButton.place(relwidth=.25, relheight=0.10, relx=.75, rely=.9)
 
#Previous button group 
previousImage = PhotoImage(file='image_files/previous.png')

def previousAudio():
    global buttonCounter, song
    buttonCounter *= 0
    if(song > 0): 
        song -= 1  
        playAudio()
    else:
        song = len(playlist) - 1 
        playAudio()

previousButton = Button(frame, image=previousImage, command = previousAudio, highlightthickness = 0)
previousButton.place(relwidth=.25, relheight=0.10, relx=0, rely=.9)

#Queue song (auto)
def playNext():
    global buttonCounter, song
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        buttonCounter *= 0
        song += 1
        if(song == len(playlist)):
            song = 0 
        playAudio()
    root.after(1, playNext)

#Volume slider group    
def changeVolume(vol):
    volume = float(vol)/100
    mixer.music.set_volume(volume)

volumeSlider = ttk.Scale(frame, from_ = 100, to = 0, command = changeVolume, orient=VERTICAL) 
style = ttk.Style()
style.theme_use('clam') 
style.configure("TScale", gripcount=0,
background="black", darkcolor="grey90", lightcolor="Lightgrey",
troughcolor="white", bordercolor="grey70", arrowcolor="white")         
volumeSlider.set(25) 
mixer.music.set_volume(25)
volumeSlider.place(relwidth=.05, relheight=0.29, relx=.94, rely=.60)

#Prevent window resizing
root.resizable(False, False) 

#Keep program running 
root.mainloop()