import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def texttospeech(text,filename):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeaudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateskeleton():
    # 1 Generate Kripya dhayan dijye
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioprocessed = audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")
    

    
    #- 3Generate Se chalkar 
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 91000
    finish = 92200
    audioprocessed = audio[start:finish]
    audioprocessed.export("3_hindi.mp3", format="mp3")
    
    
    
    # 5 -Generate se chalkar
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 94000
    finish = 95200
    audioprocessed = audio[start:finish]
    audioprocessed.export("5_hindi.mp3", format="mp3")
    
    
    
    # 7 - Generate ko jaane waali sankhya
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 96000
    finish = 98900
    audioprocessed = audio[start:finish]
    audioprocessed.export("7_hindi.mp3", format="mp3")
    
    
    
    # 9 -generate kux hi samay m platform sankhya
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 105000
    finish = 108200
    audioprocessed = audio[start:finish]
    audioprocessed.export("9_hindi.mp3", format="mp3")
    
    
    # 11- generate pr aa rhi h
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 109000
    finish = 112250
    audioprocessed = audio[start:finish]
    audioprocessed.export("11_hindi.mp3", format="mp3")
    
     

def generateannouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        # 2 -Generate From city
        texttospeech(item['from'], '2_hindi.mp3')
        
        # 4- Generate via -city
        texttospeech(item['via'], '4_hindi.mp3')
        
        # 6- Generate to-city
        texttospeech(item['to'], '6_hindi.mp3')
        
        # 8 - Generate train  no. and name
        texttospeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        
        # 10- Generate platform-number
        texttospeech(item['platform'], '10_hindi.mp3')
        
        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        
        announcement = mergeaudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton.. ")
    generateskeleton()
    print("Now Generating Announcement..")
    generateannouncement("announce_hindi.xlsx")
    
    