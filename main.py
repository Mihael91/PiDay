import pygame
from mido import Message, MidiFile, MidiTrack
import subprocess

velicina = int(input("Upisi broj znamenki za generiranje nota: "))
note = []
mid = MidiFile()
melodija = MidiTrack()
mid.tracks.append(melodija)

with open("pi_2000000.txt") as file:
    brojevi = file.read().replace("\n", "")

for i in range(velicina):
    match int(brojevi[i]):
        case 0:
            temp = 60 # "c"
        case 1:
            temp = 62 # "d"
        case 2:
            temp = 64 # "e"
        case 3:
            temp = 65 # "f"
        case 4:
            temp = 67 # "g"
        case 5:
            temp = 69 # "a"
        case 6:
            temp = 71 # "b"
        case 7:
            temp = 72 # "c'"
        case 8:
            temp = 74 # "d'"
        case 9:
            temp = 76 # "e'"
    melodija.append(Message('note_on', note=temp, velocity=64, time=200))
    melodija.append(Message('note_off', note=temp, velocity=64, time=200))

mid.save('pimelodija.mid')
musescore_path = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
command = [musescore_path, 'pimelodija.mid', "-o", 'glazbene_note.pdf', "--style", 'compress.mss']

subprocess.run(command)
subprocess.run(["start", 'glazbene_note.pdf'], shell=True)

pygame.init()
pygame.mixer.music.load("pimelodija.mid")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue



    