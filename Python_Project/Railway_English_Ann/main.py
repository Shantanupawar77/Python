import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - generate May have attention plz
    start = 18000
    finish = 22000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")
    # 2 train number
    start = 22000
    finish = 24000
    audioProcessed = audio[start:finish]
    audioProcessed.export("2_english.mp3", format="mp3")

    # 3 - Actual train number 
    # 4 - train name 
    # 5-from
    start = 30500
    finish =31200
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")
    
    # 6 to 
    start = 32000
    finish =32500
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")
    # 7 via 
    start = 33200
    finish =34200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 8 arrival at platform 
    start = 36000
    finish = 40500
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_english.mp3", format="mp3")

    # 9 platform number




    

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 3 - Generate train number
        textToSpeech(item['train_no'], '3_english.mp3')

        # 4 - Generate train name
        textToSpeech(item['train_name'], '4_english.mp3')

        # 6 - Generate from 
        textToSpeech(item['from'], '6_english.mp3')

        # 8 - Generate to 
        textToSpeech(item['to'], '8_english.mp3')

        # 10 - Generate via 
        textToSpeech(item['via'], '10_english.mp3')
        # 11 - platform number 
        textToSpeech(item['platform'], '12_english.mp3')

        
        audios = [f"{i}_english.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['train_name']}_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_engl.xlsx")