import os, subprocess, time
from check_list import check_folders


# Gets the information regarding a file
def open_file(name):
    name = '"' + name + '"'
    try:
        s = resolve_info(str((subprocess.check_output("cd c:/ && dir " + name + " /s /p", shell=True))).split("of")[1], name)
    except Exception as e:
        s = "This file does not exist, make sure you typed the name correctly"
    return s

# Resolves the string that the CMD returned
def resolve_info(output, name):
    pathntime = output.split("       ")[0]
    size = output.split("       ")[1].split(" ")
    for x in size:
        if x.startswith("1") or x.startswith("2") or x.startswith("3") or x.startswith("4") or x.startswith("5") or x.startswith("6") or x.startswith("7") or x.startswith("8") or x.startswith("9"):
            size = x
            break
    size = str(int(size.replace(",", "")) / 1000)
    pathntime = pathntime.split('n\r')[0].split("\\r\\n\\r\\n")
    path = pathntime[0].split("\\\\")
    time = pathntime[1]
    s = ""
    for p in path:
        s += p + " ---> "
    s += name
    return "Location: "+s+"\n"+"Last edited: "+time+"\n"+"Size: "+size+" kilobytes"

# Starts a program
def start_program(name):
    # The list of the available programs
    special = {"fileexplorer": "explorer", "skype": "skype", "chrome": "chrome", "settings": "ms-settings:",
               "calculator": "calc", "controlpanel": "control", "devicemanager": "devmgmt.msc",
               "taskmanager": "taskmgr", "volumemixer": "sndvol", "mediaplayer": "wmplayer","recyclingbin":"::{645FF040-5081-101B-9F08-00AA002F954E}",
               "word": "winword", "powerpoint": "powerpnt.exe", "excel": "excel.exe", "internet": "msedge.exe",
               "microsoftexplorer": "msedge.exe", "microsoftedge": "msedge.exe", "cmd": "cmd"}
    keys = []
    for key in special.keys():
        keys.append(key)
    if name in keys:
        # Opens the program
        os.system("start " + special.get(name))
        time.sleep(1.5)
        s = name + " was successfully opened "
    # If the name is not in the special ones it checks the existence of the program
    else:
        name = name +".exe"
        # Activates the function tht opens the program
        p = open_file(name)
        # Understands whether the program exists or not according to the "open_file" function response
        if p != "This file does not exist, make sure you typed the name correctly":
            s = "The system cant open this program, choose only from the program list"
        else:
            s = "This file does not exist, make sure you typed the name correctly"
    return s

# Closes programs
def close_process(name):
    # A list of programs with a specific name that the CMD will recognize
    special = {"fileexplorer": "explorer.exe", "skype": "skype.exe", "chrome": "chrome.exe", "settings": "ms-settings:",
               "calculator": "calc", "controlpanel": "control", "devicemanager": "devmgmt.msc",
               "volumemixer": "sndvol.exe", "mediaplayer": "wmplayer.exe",
               "word": "winword.exe", "TaskManager": "taskmgr", "powerpoint": "powerpnt.exe", "excel": "excel.exe", "internet": "msedge.exe",
               "microsoftexplorer": "msedge.exe", "microsoftedge": "msedge.exe"}
    keys = []
    for key in special.keys():
        keys.append(key)
    if name in keys:
        subprocess.check_output("taskkill /f /im  "+special.get(name))
        if name == "fileexplorer":
            os.system("start explorer.exe")
        if name == "TaskManager":
            return "Task Manager can't be terminated. Reason: Access is denied"
    else:
        name = '"'+name+'.exe"'
        try:
            subprocess.check_output("taskkill /f /im  "+name)
        except Exception as e:
            return "This program does not exist"
    return "Dealt with"

# Creates a note in the computer directories
def create_note(name):
    # Checks the existence of the directory the notes are in
    check_folders()
    name1 = os.path.join('C:/Amanda-assist/Notes', name+".txt")
    file1 = open(name1, "w")
    file1.close()
    return "List about " + name + " has been created"

# Lists all of the notes
def all_notes():
    check_folders()
    all_of_them = os.listdir('C:/Amanda-assist/Notes')
    s = ""
    for x in range(len(all_of_them)):
        s += all_of_them[x].replace("'", "").replace(".txt", "")+"\n"
    return s

# Shows the information about a specific note
def show_info(name):
    check_folders()
    if not os.path.isfile('C:/Amanda-assist/Notes/'+name):
        return "the note you are looking for does not exist"
    if len((open('C:/Amanda-assist/Notes/'+name, "r")).read()) == 0:
        return "The list is empty"
    return "your list says: " + (open('C:/Amanda-assist/Notes/'+name, "r")).read()

# Edits the information written in a specific note
def edit_note(name, information):
    check_folders()
    if not os.path.isfile('C:/Amanda-assist/Notes/'+name):
        return "the note you are looking for does not exist"
    f = open('C:/Amanda-assist/Notes/'+name, "r+")
    f.truncate(0)
    name = name.split(".txt")[0]
    f.write(information)
    f.close()
    return "List about " + name + " has been edited"





