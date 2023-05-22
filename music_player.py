import pygame
import os
from tkinter import Tk, Button, Label, Listbox, END
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()
    
def stop_music():
    pygame.mixer.music.stop()
    
def unpause_music():
    pygame.mixer.music.unpause()
    
def on_play_button():
    selection = song_listbox.curselection()
    if len(selection) > 0:
        selected_song = songs[selection[0]]
        file_path = os.path.join(music_directory, selected_song)
        play_music(file_path)

def list_songs(directory):
    songs = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            songs.append(file)
    return songs
def on_stop_button():
    stop_music()
    
def on_pause_button():
    pause_music()

def on_resume_button():
    unpause_music()
pygame.init()
pygame.mixer.init()

music_directory = "C:/Users/venuk/Downloads"

songs = list_songs(music_directory)

root = Tk()
root.title("Music Player")

song_label = Label(root, text="Select a song to play:")
song_label.pack()

song_listbox = Listbox(root)
song_listbox.pack()

for song in songs:
    song_listbox.insert(END, song)

stop_button = Button(root, text="Stop", command=on_stop_button)
stop_button.pack()

play_button = Button(root, text="Play", command=on_play_button)
play_button.pack()

pause_button = Button(root, text="Pause", command=on_pause_button)
pause_button.pack()

resume_button = Button(root, text="Resume", command=on_resume_button)
resume_button.pack()

root.mainloop()
