import socket, pyttsx3, PIL, tkinter, time, os
from check_list import *
from task_sorter import *
from spellchecker import SpellChecker
from tkinter import *
from PIL import ImageTk, Image
# Different exit the program options
goodbye = ["bye", "goodbye", "have a good one", "see you", "see u", "take care", "bye bye", "thanks for your help", "thanks for the help", "takecare"]


def send(EntryBox, ChatLog, base):
    # Gets the username
    name = check_names()[0]
    # Gets the user's massage from the entry box
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    # When the user exists and the loop ends the client sends a goodbye massage so the server knows to shut down
    if msg in goodbye:
        mes = "bye"
        mes = mes.encode()
        my_socket.send(mes)
        base.destroy()
        exit()
    # If the user's massage is blank the program wont enter this loop and wont present anything
    elif msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, name+": " + msg + '\n\n')
        ChatLog.config(foreground="white", font=("Times", 12, "normal"))
    mes1 = msg.lower()
    count1 = mes1.count(" ")
    mes2 = spell.correction(mes1)
    count2 = mes2.count(" ")
    # Makes sure the spell correction model doesn't remove any words from the request
    # It compering the length of the request to the length of the corrected request
    if not count1 == count2:
        mes = mes1
    else:
        mes = mes2
    mes = mes.encode()
    my_socket.send(mes)
    data = my_socket.recv(1024)
    data = data.decode()
    # Gets the data which is function number and function content and sends it to the script that activates functions
    data = sort_tasks(data)
    namea = check_names()[1]
    # Presents the assistant's response
    ChatLog.insert(END, namea+": " + data + '\n\n')
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)
    data = data.split("\n")
    s = ""
    for x in range(len(data)):
        s += data[x]+" "
    time.sleep(1.5)
    # Says the response
    engine.say(s)
    engine.runAndWait()

# When the user goes to the chat screen from the home screen this function creates the chat screen
def log(base):
    base.destroy()
    base = Tk()
    base.title("Personal Assistant")
    base.geometry("390x500")
    base.resizable(False, False)
    photo = PhotoImage(file=r"C:\PycharmProjects\Big_Project\Network\care.png")
    base.iconphoto(False, photo)
    # Creates Chat window
    ChatLog = Text(base, bd=0, bg="black", height="90", width="70", font=("Times", 10, "normal"))
    ChatLog.config(state=DISABLED)
    # Binds scrollbar with the Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="pirate")
    ChatLog['yscrollcommand'] = scrollbar.set
    SendButton = Button(base, font=("Verdana", 10, 'bold'), text="Send your \n request", width="12", height="5", bd=0, bg="orange2", activebackground="gray80", fg='#ffffff', command=lambda: send(EntryBox, ChatLog, base))
    # Create send Button
    EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font=("David", 12, "normal"))#Create the box to enter message
    # Place all components on the screen
    scrollbar.place(x=376, y=2, height=406)
    ChatLog.place(x=4, y=4, height=406, width=372)
    EntryBox.place(x=124, y=415, height=80, width=253)
    SendButton.place(x=4, y=415, height=80)
    name = check_names()[0]
    base.mainloop()


# Sets the spell checker
spell = SpellChecker()
# Sets the assistant's speech including speed and voice
engine = pyttsx3.init()
rate = engine.getProperty('rate')-35
engine.setProperty('rate', rate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Activates the function to find the path to google chrome
find_google()
# Activates the function to install pip packages
install_things()
# Tries to remove th google cookie list that is generated by the requests package
try:
    os.remove(".google-cookie")
except Exception as e:
    None
ip = '127.0.0.1'
port = 4000
my_socket = socket.socket()
my_socket.connect((ip, port))
# Gets the username
name = check_names()[0]
# Sets the tkinter window, the size, the icon
base = Tk()
base.title("Personal Assistant")
base.geometry("500x281")
base.resizable(False, False)
photo = PhotoImage(file=r"C:\PycharmProjects\Big_Project\Network\care.png")
base.iconphoto(False, photo)
img = PIL.Image.open(r"C:\PycharmProjects\Big_Project\Network\back.jpg").convert("RGB")
ph = ImageTk.PhotoImage(img)
# Creates a "canvas" that allows to wright things and create buttons on the interface and set a backround
canvas = Canvas(base, width=500, height=281)
canvas.pack(fill="both", expand=True)
# Creates the backround
canvas.create_image(0, 0, image=ph, anchor="nw")
# Create the text
canvas.create_text(245, 35, text="Hello Dir "+name, font=("Helvetica", 20), fill="#F9E547")
canvas.create_text(92, 265, text="Project By Ron Aharonovich", font=("Times", 12), fill="#F9E547")
canvas.create_text(405, 265, text="Your Own Personal Assistant", font=("Times", 12), fill="#F9E547")
# Creates the buttons
button1 = Button(base, text="Start", command=lambda: log(base))
button2 = Button(base, text="Exit", command=lambda: base.destroy())
button1_window = canvas.create_window(8, 10, anchor="nw", window=button1)
button2_window = canvas.create_window(460, 10, anchor="nw", window=button2)
# Starts the loop that checks any actions with the interface like pushing buttons and writing
base.mainloop()



