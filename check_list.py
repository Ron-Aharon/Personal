import json, subprocess, os
from random import randrange

# names of pip packages that need to be installed
name = ["pyttsx3", "image", "requests", "google", "google-search", "pathlib", "bs4", "youtube_search", "axju-jokes"]

# Finds the location of google Chrome browser on the computer
def find_google():
    with open("google.json", "r") as read_file:
        path = json.load(read_file)
    if path == "":
        s = str((subprocess.check_output('cd c:/ && dir "chrome.exe" /s /p', shell=True))).split("of")[1]
        pathntime = s.split("       ")[0]
        pathntime = pathntime.split('n\r')[0].split("\\r\\n\\r\\n")
        path = pathntime[0].split("\\\\")
        s = path[0].strip(" ") + "//"
        for p in range(1, len(path)):
            s += path[p] + "//"
        s += "chrome.exe"
        with open("google.json", "w") as read_file:
            json.dump(s, read_file)


# Returns the names of the assistant and the user
def check_names():
    with open("name.json", "r") as read_file:
        name = json.load(read_file)
    with open("namea.json", "r") as read_file:
        namea = json.load(read_file)
    return name, namea

# Checks the existence of the directory with the notes
def check_folders():
    if not os.path.isdir('C:/Amanda-assist/Notes'):
        os.makedirs('C:/Amanda-assist/Notes')

# Returns a rendom number
def random(len):
    return randrange(len)

# installs all of the pip packages
def install_things():
    for x in name:
        subprocess.check_output("pip install " + x, shell=True)
