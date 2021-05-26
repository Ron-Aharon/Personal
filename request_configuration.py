# Gets the user's command and understand it. Sends a string with the number of the command and its content to the task sorter
def understand(command):
    if command == "what is the time" or command == "what time is it" or command == "tell me the time please" or command == "tell me the time":
        return "1@@@@ "
    if command.startswith("open website") or command.startswith("search for"):
        p = command.split(" ")
        s = ""
        for x in range(2, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "3@@@@"+s
    if command.startswith("open the website of") or command.startswith("please search google for") or command.startswith("search the web for") or command.startswith("search the internet for"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "3@@@@"+s
    if command.startswith("please open website") or command.startswith("please search for") or command.startswith("search google for"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "3@@@@"+s
    if command.startswith("please open the website of") or command.startswith("please search the web for") or command.startswith("please search the internet for"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "3@@@@"+s
    if command.startswith("change assistant's name to") or command.startswith("change assistants name to") or command.startswith("change your name to"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "4@@@@"+s
    if command.startswith("please change assistant's name to") or command.startswith("please change assistants name to") or command.startswith("please change your name to"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "4@@@@"+s
    if command.startswith("change username to") or command.startswith("change user-name to"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "5@@@@"+s
    if command.startswith("please change username to") or command.startswith("change user name to") or command.startswith("change my name to"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "5@@@@"+s
    if command.startswith("please change user name to") or command.startswith("please change my name to"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "5@@@@"+s
    if command.startswith("check the existence of the file"):
        p = command.split(" ")
        s = ""
        for x in range(6, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "6@@@@"+s
    if command.startswith("check file exists"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "6@@@@"+s
    if command.startswith("please check file exists"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "6@@@@"+s
    if command.startswith("please check the existence of the file"):
        p = command.split(" ")
        s = ""
        for x in range(7, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "6@@@@"+s
    if command.startswith("run") or command.startswith("start") or command.startswith("open"):
        p = command.split(" ")
        s = p[1]
        if len(p) == 3:
            s += p[2]
        return "7@@@@"+s
    if command.startswith("please run") or command.startswith("please start") or command.startswith("please open"):
        p = command.split(" ")
        s = p[2]
        if len(p) == 4:
            s += p[3]
        return "7@@@@"+s
    if command.startswith("close") or command.startswith("stop") or command.startswith("terminate"):
        p = command.split(" ")
        s = p[1]
        if len(p) == 3:
            s += p[2]
        return "8@@@@"+s
    if command.startswith("please close") or command.startswith("please stop") or command.startswith("please terminate"):
        p = command.split(" ")
        s = p[2]
        if len(p) == 4:
            s += p[3]
        return "8@@@@"+s
    if command.startswith("ask google") or command.startswith("find out"):
        p = command.split(" ")
        s = ""
        for x in range(2, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "9@@@@"+s
    if command.startswith("please ask google") or command.startswith("please find out "):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "9@@@@"+s
    if command.startswith("define"):
        p = command.split(" ")
        s = p[1]
        if len(p) > 2:
            for x in range(1, len(p)):
                s += p[x]+"-"
        return "10@@@@"+s
    if command.startswith("please tell me what is the definition of"):
        p = command.split(" ")
        s = p[8]
        if len(p) > 9:
            for x in range(8, len(p)):
                s += p[x]+"-"
        return "10@@@@"+s
    if command.startswith("please tell me the definition of"):
        p = command.split(" ")
        s = p[6]
        if len(p) > 7:
            for x in range(6, len(p)):
                s += p[x]+"-"
        return "10@@@@"+s
    if command.startswith("please define"):
        p = command.split(" ")
        s = p[2]
        if len(p) > 3:
            for x in range(2, len(p)):
                s += p[x]+"-"
        return "10@@@@"+s
    if command.startswith("play"):
        p = command.split(" ")
        s = ""
        for x in range(1, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "11@@@@"+s
    if command.startswith("please play"):
        p = command.split(" ")
        s = ""
        for x in range(2, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "11@@@@"+s
    if command.startswith("open on map"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("please open on map"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("open on map"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("open on map the location of") or command.startswith("please open on map the location"):
        p = command.split(" ")
        s = ""
        for x in range(6, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("open on map the location"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("please open on map"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "12@@@@"+s
    if command.startswith("please open on map the location of"):
        p = command.split(" ")
        s = ""
        for x in range(7, len(p)):
            s += p[x]+" "
        s += p[len(p)-1]
        print(s)
        return "12@@@@"+s
    if command == "turn off the computer" or command == "turn off" or command == "please turn off" or command == "shut down" or command == "please turn off computer" or command == "please turn off the computer" or command == "please shut down" or command == "shut down the computer" or command == "please shut down the computer":
        return "13@@@@"
    if command.startswith("create a list regarding") or command.startswith("create a list about"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "14@@@@"+s
    if command.startswith("please create a list regarding") or command.startswith("please create a list about"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "14@@@@"+s
    if command == "list all of the notes" or command == "list all of the lists" or command == "list all of the lists please" or command == "list all of my lists please" or command == "list all of my lists" or command == "list all of my notes" or command == "please list all of the notes" or command == "please list all of my notes" or command == "show all of the notes" or command == "show all of my notes" or command == "please show all of the notes" or command == "please show all of my notes":
        return "15@@@@ "
    if command.startswith("show the information regarding") or command.startswith("show the information about"):
        p = command.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        s = s + ".txt"
        return "16@@@@"+s
    if command.startswith("please show the information regarding") or command.startswith("please show the information about"):
        p = command.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        s = s + ".txt"
        return "16@@@@"+s
    if command.startswith("edit the information regarding") or command.startswith("edit the information about") or command.startswith("edit the list regarding") or command.startswith("edit the list about"):
        p = command.split(". please write: ")
        name = p[0]
        information = p[1]
        p = name.split(" ")
        s = ""
        for x in range(4, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        s = s + ".txt" + "()" + information
        return "17@@@@"+s
    if command.startswith("please edit the information regarding") or command.startswith("please edit the information about") or command.startswith("please edit the list regarding") or command.startswith("please edit the list about"):
        p = command.split(". please write: ")
        name = p[0]
        information = p[1]
        p = name.split(" ")
        s = ""
        for x in range(5, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        s = s + ".txt" + "()" + information
        return "17@@@@"+s
    if command.startswith("please say"):
        p = command.split(" ")
        s = ""
        for x in range(2, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "18@@@@"+s
    if command.startswith("can you say"):
        p = command.split(" ")
        s = ""
        for x in range(3, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "18@@@@"+s
    if command.startswith("say"):
        p = command.split(" ")
        s = ""
        for x in range(1, len(p)-1):
            s += p[x]+" "
        s += p[len(p)-1]
        return "18@@@@"+s
    if command == "ok" or command == "fine" or command == "whatever" or command == "ok fine" or command == "k" or command == "okay":
        return "19@@@@"
    if command == "ok thanks" or command == "thank you" or command == "thanks" or command == "oh thanks" or command == "thanks a lot" or command == "tnks" or command == "ok great" or command == "great" or command == "good" or command == "oh great" or command == "thanks for your help":
        return "20@@@@"
    if command == "give me a joke" or command == "please give me a joke" or command == "give me a joke please" or command == "tell me a joke" or command == "please tell me a joke" or command == "tell me a joke please" or command == "can you tell me a joke please" or command == "can you give me a joke please" or command == "can you tell me a joke" or command == "can you give me a joke":
        return "21@@@@"
    if command == "give me a quote" or command == "please give me a quote" or command == "give me a quote please" or command == "tell me a quote" or command == "please tell me a quote" or command == "tell me a quote please" or command == "can you tell me a quote please" or command == "can you give me a quote please" or command == "can you tell me a quote" or command == "can you give me a quote":
        return "22@@@@"
    if command == "how old are you" or command == "what is your age" or command == "what's your age" or command == "tell me your age" or command == "please tell me your age" or command == "tell me your age please" or command == "can you tell me your age please" or command == "can you tell me your age":
        return "23@@@@"
    if command == "will you marry me" or command == "i dare you to marry me" or command == "marry me please" or command == "marry me will you":
        return "24@@@@"
    if command == "are you single" or command == "do you have a bf" or command == "do you have a boy friend":
        return "25@@@@"
    if command == "i love you" or command == "i think i love you" or command == "im in love with you" or command == "i'm in love with you" or command == "i think im in love with you" or command == "i think I'm in love with you":
        return "26@@@@"
    if command == "who is your founder" or command == "who is your father" or command == "who created you" or command == "who is your creator" or command== "who are your parents" or command == "who did create you" or command == "who founded you":
        return "27@@@@"
    if command == "wow" or command == "oh really" or command == "really":
        return "28@@@@"
    if command == "you are smart" or command == "you are really smart" or command == "you are beautiful" or command == "you are really beautiful" or command == "you are super helpful" or command == "you are really helpful" or command == "you are helpful":
        return "29@@@@"
    if command == "what can you do" or command == "please tell me what can you do" or command == "what can you do":
        return "30@@@@"
    if command == "who is your owner":
        return "31@@@@"
    if command == "how can i call you" or command == "what is your name" or command == "how can i name you" or command == "can you tell me your name" or command == "can you please tell me your name" or command == "can you please tell me your name please":
        return "32@@@@"
    if command == "how are you" or command == "what's up" or command == "what's poppin" or command == "whats up" or command == "whats poppin" or  command == "hey how are you" or command == "hey what's upp" or command == "hey what's poppin" or command == "hey whats upp" or command == "hey whats poppin":
        return "33@@@@"
    if command == "hey" or command == "hi" or command == "hi there" or command == "hello" or command == "hello to you":
        return "34@@@@"
    if command == "what is my name" or command == "can you tell me my name" or command == "tell me my name please" or command == "can you tell me my name please" or command == "tell me my name":
        return "35@@@@"
    else:
        return "2@@@@ "




