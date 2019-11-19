"""
Install this two library using command promote rus as admin
pip install gTTS
pip install playsound
"""

# Import the required module for text  
# to speech conversion 
from gtts import gTTS

# This module is imported so that we can  
# play the converted audio 
import playsound
import os

# The text that you want to convert to audio 
mytext = 'হ্যালো স্যার! আমি আপনার সহকারি। দয়াকরে বলুন কিভাবে আপনাকে সাহায্য করতে পারি?'
  
# Language in which you want to convert 
language = 'bn'

# Create temperory file
filename = 'temp.mp3'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed
tts = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3  
tts.save(filename)

# Playing the converted file 
# os.system("mpg321 temp.mp3")
playsound.playsound(filename, True)

# Remove temperory file 
os.remove(filename)
