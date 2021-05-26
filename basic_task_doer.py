import datetime, os, subprocess, webbrowser, json, sys, requests, os.path, re, time, urllib.request
from googlesearch import search
from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from urllib.request import urlopen
from youtube_search import YoutubeSearch
from check_list import *
from check_list import *

# The assistant's responses for specific tasks
dont_know = ["I dont know", "I have no idea", "Sorry couldn't find it out", "I have no knowledge about that"]
problem = "The is a grammatical article in English, denoting persons or things already mentioned, under discussion, implied or otherwise presumed familiar to listeners, readers or speakers. It is the definite article in English."
website = ["The website you requested was opened", "I found what you were looking for", "Here you go", "Check this out", "I found something"]

# Checks the time and resolves the information
def time_check():
    t = str(datetime.datetime.now()).split(" ")
    t1 = t[0].split("-")
    t2 = t[1].split(":")
    return t2[0]+":"+t2[1]+"  "+t1[1]+"/"+t1[2]+"/"+t1[0]

# Opens the website the user asks for
# Returning the top 10 domains about a topic and opens the first one
def open_website(website_name):
    with open("google.json", "r") as read_file:
        my_file = Path(json.load(read_file))
    for j in search(website_name, tld="co.in", num=10, stop=1, pause=2):
        if my_file.is_file():
            # Gets the location of google chrome from a generated json file
            with open("google.json", "r") as read_file:
               x = json.load(read_file)
            # Sets google chrome as the browser
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(x))
            # Opens up the site
            webbrowser.get('chrome').open(j)
        else:
            webbrowser.open_new_tab(j)
    time.sleep(1.5)
    return website[random(5)]

# Changes assistant's name
def change_assistants_name(name):
    name = name.split(" ")
    # Makes sure the name starts with a capital letter even if it has more than 1 word in it
    if len(name) == 1:
        s = name[0][0].upper()+name[0][1:]+" "
    else:
        s = ""
        for x in range(len(name)-1):
            s += name[x][0].upper()+name[x][1:]+" "
        s += name[x][0].upper()+name[len(name)-1][1:]
    with open("namea.json", "w") as write_file:
        json.dump(s, write_file)
    x = random(2)
    if x == 0:
        return "I changed the name to " + s
    return "The name was changed to " + s

# Changes username
def change_username(name):
    name = name.split(" ")
    s = ""
    for x in range(len(name)-1):
        s += name[x][0].upper()+name[x][1:]+" "
    s += name[x][0].upper()+name[len(name)-1][1:]
    with open("name.json", "w") as write_file:
        json.dump(s, write_file)
    x = random(2)
    if x == 0:
        return "I changed the name to " + s
    return "The name was changed to " + s

# Scraps the web for an answer for the question
def ask_google(search):
    # Gets the google's answer to the question
    url = f"https://www.google.com/search?q={search}"
    request = requests.get(url)
    to_translate = str((BeautifulSoup(request.text, "html.parser")).find("div", "BNeawe").text)
    # If the answer is not just numbers it translates it in case there are things in other languages
    if not to_translate.isnumeric():
        answer = (GoogleTranslator(source='auto', target='english').translate(to_translate)).split(" ")
    else:
        return to_translate
    # If the answer is too short it means that google did not provide a good answer
    # The scrip scrapes information from wikipedia
    if len(answer) < 2:
        search2 = search.split(" ")[2]
        r = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/"+search2)
        page = r.json()
        try:
            answer = page.get("extract").split(".")
        # If there is an error the program tells so
        except AttributeError:
            return "I have no knowledge about "+search2
        answer = answer[0]+"."+answer[1]+"."
        # If the answer is a spesific string that wikipedia gives in case there isn't an answer the assistant wil tell it doesn't know the answer
        if answer == problem:
            return dont_know[random(3)]
        answer = answer.split(" ")
    # Organizes the string google returnes
    if len(answer) > 10:
        s = ""
        counter = 0
        for x in range(len(answer)):
            s += answer[x] + " "
            counter += 1
            if counter % 10 == 0:
                s += "\n"
        return s
    return GoogleTranslator(source='auto', target='english').translate(to_translate)

# Defines a word
def define(word):
    # Uses an API of an internet site to scrab the defenition
    # Than decodes it to a string
    # In case of an error it says the word was not found
    try:
        use = urllib.request.urlopen("http://dictionary.reference.com/browse/"+str(word)+"?s=t").read().decode('utf-8')
    except:
        return "Word was not found"
    # Cleans the string and removes the unnecessary parts in the string
    items = re.findall('<meta name="description" content="'+".*$", use, re.MULTILINE)
    y = items[0].replace('<meta name="description" content="', ' ')
    z = y.replace(' See more.">', '')
    if 'definition at Dictionary.com, a free online dictionary with pronunciation, synonyms and translation' in z:
        return "Word was not found"
    answer = z.split(" ")
    if len(answer) > 10:
        s = ""
        counter = 0
        for x in range(len(answer)):
            s += answer[x] + " "
            counter += 1
            if counter % 10 == 0:
                s += "\n"
        return s
    return z[1:]

# Plays a song\a youtube video
def play_youtube(song):
    # Gives the top results from a youtube search
    results = YoutubeSearch(song, max_results=1).to_json()
    # Gets the special ending of the video's URL
    link = results.split('"url_suffix": ')
    link = link[1][:-4][1:]
    # Connects the ending to the main URL
    link = "https://www.youtube.com"+link
    # Opens the link like it opens a website
    open_website(link)
    time.sleep(1.5)
    x = random(5)
    if x == 0:
        return "Here you go"
    if x == 1:
        return "Here listen to what I found"
    if x == 2:
        return "I found something"
    if x == 3:
        return "I opened " +song+ " on Youtube"
    if x == 4:
        return '"'+song+'" is now playing'

# Opens the location in google maps
def open_map(place):
    link = 'https://www.google.com/maps/place/' + place
    webbrowser.open_new_tab(link)
    time.sleep(1.5)
    x = random(5)
    if x == 0:
        return "Here you go"
    if x == 1:
        return "Here look at what I found"
    if x == 2:
        return "I opened the location up in Google maps"
    if x == 3:
        return "I opened " +place+ " on Google maps"
    if x == 4:
        return "I have found " + place + " in Google maps"

# Turns off the computer
def turn_off():
    os.system("shutdown /s /t 1")





