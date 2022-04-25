# Import library
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import pyaudio
import pygame
import pandas as pd
import random
import os

# Tìm keyword từ text, keyword from question column of dataframe
def findKeyword(text,listKW):
    for kw in listKW:
        if kw in text.lower():
            return kw

# Speech to text using google api
def speechToText():
    with sr.Microphone() as source2:
        audio = r.listen(source2)
        text = r.recognize_google(audio, language="vi-VI")
        return text

# Random answer from list answers where question data = keyword
def randomAnswer(keyword , data):
    dfByKeyword = data[data["question"]==keyword]
    if dfByKeyword.empty==False:
        answers = dfByKeyword["answer"].tolist()
        an = answers[0].split("-")
        return random.choice(an)
    else: return "Câu hỏi của bạn không có trong danh sách"

# Convert text to speech using gtts
def textToSpeech(text):
    tts = gTTS(text,lang='vi', slow=False)
    tts.save("Result.mp3")
    playsound("Result.mp3")
    os.remove("Result.mp3")

# Regconize and answer
def regconize(df):
    textToSpeech("Xin chào. Bạn cần tôi giúp gì?")
    text= speechToText() 
    if text.lower() == "rô bốt":
        listKeyword = df["question"].values      
        keyword = findKeyword(text,listKeyword)
        answer = randomAnswer(keyword, df)
        textToSpeech(answer)

def addQuestion():
    print("add a row in csv")

# Main program
df = pd.read_csv("cauhoi.csv") # Read csv file
r = sr.Recognizer()    # Initialize the recognizer
while (1):
    try:
        regconize(df)
    except sr.RequestError as e:
        print("Lỗi request; {0}".format(e))
    except sr.UnknownValueError:
        print("Không nhận dạng được")