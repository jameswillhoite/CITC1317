#!/bin/python
"""
James Willhoite
10/18/19
Lab 7 Chatbot
"""
import random
import time
import re
import datetime

def getResponse(line):
    global myname, name
    words = line.split()
    if words[0] == 'why' or words[0] == 'do' or words[0] == 'what':
        return askedQuestion(line, words)
    elif 'how are you' in line:
        return 'I\'m doing great! How are you?'
    elif 'nice' in line and 'meet you' in line:
        return "It is nice to meet you too " + name + "."
    elif 'tell' in line and 'me' in line:
        if 'joke' in line:
            return tellJoke()
    elif ('i will' in line and 'call you' in line) or ('change your name' in line):
        x = re.findall('(?:call\syou\s|your\sname|name\s)\s(?:to)?\s([a-z\s]*)', line)
        myname = x[0].title()
        return "Ok. My name is now " + myname
    elif ('change my' in line and 'name' in line) or ('call me' in line):
        x = re.findall('(?:change\smy\sname)\s(?:to)\s([a-z\s]*)', line)
        name = x[0].title()
        return "Ok. I will now call you " + name
    elif ('good one' in line) or ('you\'re awesome' in line) or ('that\'s awesome' in line):
        return recieveComplement()
    elif 'give' in line and 'complement' in line:
        return giveComplement()

    return "Can you tell me a little more about that ...."


def askedQuestion(line, words):
    if 'who i am' in line:
        return "Yes, your name is " + name
    elif 'what' in line:
        today = datetime.datetime.now()
        if 'your name' in line:
            return "My name is " + myname + "."
        if 'my name' in line:
            return "Your name is " + name
        if 'day' in line:
            return 'Today is ' + today.strftime("%A")
        if 'time' in line:
            return "The time is " + today.strftime("%I:%M %p")

        reg = re.findall('([0-9]+|[0-9]+\.[0-9]+)\s?([\+\-\/\*])\s?([0-9]+|[0-9]+\.[0-9]+)', line)
        if len(reg) > 0:
            try:
                tot = eval(reg[0][0] + reg[0][1] + reg[0][2])
                return "The answer is " + str(tot)
            except:
                return "Hmm ... I'm not able to do that calculation at this time"

    '''Default'''
    return 'I\'m not sure what you are asking...'


def tellJoke():
    jokes = [
        "What do you call a dinosaur that is sleeping?",
        "What is fast, loud and crunchy?",
        "Why did the teddy bear say no to dessert?",
        "What has ears but cannot hear?",
        "What did the left eye say to the right eye?",
        "What do you get when you cross a vampire and a snowman?",
        "What did one plate say to the other plate?",
        "Why did the student eat his homework?",
        "When you look for something, why is it always in the last place you look?",
        "What is brown, hairy and wears sunglasses?",
        "Man who walk in front of car gets tired, man who walk behind car get exhausted.",
        "Man who not poop for many days must deal with backlog.",
        "Man who cut self while shaving lose face.",
        "Man who leap off cliff, jump to conclusion.",
        "Man who walk through airport turnstyle sideways going to Bangkok.",
        "Man who sneeze without tissue takes matter in own hand.",
        "Man who fart in church, sit in own pew.",
        "Wise man not keep sledge hammer and slow computer in same room."
    ]
    answer = [
        "A dino-snore!",
        "A rocket chip!",
        "Because she was stuffed.",
        "A cornfield.",
        "Between us, something smells!",
        "Frost bite!",
        "Dinner is on me!",
        "Because the teacher told him it was a piece of cake!",
        "Because when you find it, you stop looking.",
        "A coconut on vacation.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
    index = random.randint(0, len(jokes) - 1)
    joke = jokes[index]
    if len(answer[index]) > 0:
        writeToLog(myname, joke)
        print(joke + "...")
        time.sleep(2)
        return answer[index]
    else:
        return joke


def recieveComplement():
    list = [
        "Thank you.",
        "You are very kind to say that.",
        "Oh stop it ... you\'re making me blush."
    ]
    index = random.randint(0, len(list) - 1)
    return list[index]


def giveComplement():
    list = [
        "I like your style.",
        "I appreciate you.",
        "You're a smart cookie.",
        "You’re an awesome friend.",
        "You light up the room.",
        "You deserve a hug right now.",
        "Is that your picture next to “charming” in the dictionary?",
        "You’re all that and a super-size bag of chips.",
        "On a scale from 1 to 10, you’re an 11.",
        "If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.",
        "You’re like sunshine on a rainy day.",
        "You’re a great listener.",
        "Everything would be better if more people were like you!",
        "Hanging out with you is always a blast.",
        "You always know — and say — exactly what I need to hear when I need to hear it.",
        "Being around you makes everything better!",
        "You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)",
        "You’re wonderful.",
        "You’re one of a kind!",
        "You’re inspiring.",
        "You’re more fun than bubble wrap.",
        'In high school I bet you were voted “most likely to keep being awesome.”',
        "You’re really something special."
    ]
    index = random.randint(0, len(list) - 1)
    return list[index]



def writeToLog(user, txt):
    f = open("ChatBot.log", "a")
    today = datetime.datetime.now()
    text = "[" + today.strftime("%m/%d/%Y %I:%M %p") + "] " + user + ": " + txt + "\n"
    f.write(text)
    f.close()

myname = "Someone"

opening = 'Hello! My name is ' + myname + '. What\'s your name? '
writeToLog(myname, opening)

name = input(opening).title()
writeToLog(name, name)

greeting = "\nHello " + name + " it's nice to meet you.\n "
greeting += "Before we get started. If you are done talking with me, just type bye.\n"
writeToLog(myname, greeting)
print(greeting)

start = "Now, what would you like to talk about? "
writeToLog(myname, start)

line = input(start)

while line != 'bye':
    line = line.lower()
    writeToLog(name, line)

    reply = getResponse(line)
    writeToLog(myname, reply)

    line = input(reply + "\n")

closing = "It was nice talking with you " + name + ". Have a Great Day!"
writeToLog(myname, closing)
print("\n" + closing)
