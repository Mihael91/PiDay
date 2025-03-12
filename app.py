
from mido import Message, MidiFile, MidiTrack
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "POST":
        
        velicina = int(request.form["velicina"])
        action = request.form["action"]
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
        if action=="sheet":
            musescore_path = "/usr/bin/mscore" 
            command = [musescore_path, midi_path, "-o", pdf_path]

            try:
                subprocess.run(command, check=True)
                return render_template("index.html", pdf_available=True)
        elif action=="sound":
            return render_template("index.html")  

    return render_template("index.html")  

@app.route("/download-pdf")
def download_pdf():
    return send_from_directory(STATIC_DIR, "glazbene_note.pdf", as_attachment=True)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)
    
if __name__ == "__main__":
    app.run(debug=True)
