from gtts import gTTS
import os
text1="Hello I am shantanu my hobby is to code at everytime" 
# language='en'
obj=gTTS(text=text1,lang='en',slow=False)
obj.save("sample.mp3")

os.system("sample.mp3")