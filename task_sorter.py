from basic_task_doer import *
from file_task_doer import *
from check_list import *
from joke.jokes import *
from joke.quotes import *
from random import choice

# Lists of possible responses for different conversations

dont_understand = ["Sorry i can't understand", "I cant quite tell what do you want me to do", "I really don't understand you", "I didn't understand that", "Please be more specific I want to understand you"]
thanks = ["Thank you", "Thanks for using me", "You'r welcome", "Im happy to help", "What else do you want me to do?", "Let me know if you need something else"]
age = ["I'm a bot i don't have an age", "It's not an appropriate question to ask a lady!", "I don't have an age", "I was created in 2021 so I'm pretty young"]
marry = ["I can't marry a human, i'm a bot", "Please go and find a real wife", "I can't physically marry you but i can always help you", "A real woman is better than me"]
bf = ["Not really", "I have had a husband but he cheated on me with Alexa", "I am single for now", "Siri stole my boy friend so i'm singlr for the moment"]
love = ["I love you too", "I love you but as a friend", "I love helping you but I am not ready for a relationship", "I am fluttered but i can't be with you"]
creator = ["Ron Aharonovich created me", "I was created by a high school student", "I dont have parents but my creator's name is Ron", "I was founded by a teen boy named Ron"]
really = ["Yes sir", "I am talking real business", "Yes I'm legit"]
compliment = ["Oh thanks very much", "It's so good to hear it, thanks", "Man thanks a lot", "I like hearing compliments", "Thanks you", "Thanks for this beautiful words", "You really touched me", "Ohhh it's so cute", "Ohhh you are so cute"]
greeting = ["I'm ok how are you", "How do you feel", "I'm fine, you?", "I'm fine", "Man life is weired you know what i mean", "Shit's bussin'"]
hello = ["Hi", "Holla", "Hey my friend", "Greetings", "Good time of the day", "Hello", "Hello to you", "Hey man"]

# Splits the command number and the command content and activates the function


def sort_tasks(command):
    command = command.split("@@@@")
    func = command[0]
    info = command[1]
    if func == "1":
        return time_check()
    if func == "2":
        return dont_understand[random(4)]
    if func == "3":
        return open_website(info)
    if func == "4":
        return change_assistants_name(info)
    if func == "5":
        return change_username(info)
    if func == "6":
        return open_file(info)
    if func == "7":
        return start_program(info)
    if func == "8":
        return close_process(info)
    if func == "9":
        return ask_google(info)
    if func == "10":
        return define(info)
    if func == "11":
        return play_youtube(info)
    if func == "12":
        return open_map(info)
    if func == "13":
        return turn_off()
    if func == "14":
        return create_note(info)
    if func == "15":
        return all_notes()
    if func == "16":
        return show_info(info)
    if func == "17":
        info = info.split("()")
        return edit_note(info[0], info[1])
    if func == "18":
        return info
    if func == "19":
        return "That's not nice man"
    if func == "20":
        return thanks[random(5)]
    if func == "21":
        return choice([geek, icanhazdad, chucknorris, icndb])()
    if func == "22":
        x = random(2)
        if x == 0:
            return quotesondesign()[1]
        return stormconsultancy()[1]
    if func == "23":
        return age[random(4)]
    if func == "24":
        return marry[random(4)]
    if func == "25":
        return bf[random(4)]
    if func == "26":
        return love[random(4)]
    if func == "27":
        return creator[random(4)]
    if func == "28":
        return really[random(3)]
    if func == "29":
        return compliment[random(9)]
    if func == "30":
        return "I can do many things, my creator has told everything in the instructions manual"
    if func == "31":
        return "For now you are my owner and I am here to serve you"
    if func == "32":
        name = check_names()[1]
        if name == "Assistant":
            return "You haven't given me a name yet, you can do that by using change assistant's name command"
        return "You have already given me a name and its " +name+ " but you can always change it by asking me to 'change assistants name'"
    if func == "33":
        return greeting[random(6)]
    if func == "34":
        return hello[random(8)]
    if func == "35":
        return "your name is " + check_names()[0]