# -*- coding: utf-8 -*-
"""audiomix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o3L3G6yoxwMgBy3cOppuEZkUHtgubJHY
"""

from pydub import AudioSegment
import merge
audio=r"D:\Noumi\audiomixing\Audio\test"


for i in range(len(audio)-1):
    a=audio[i]
    rest_audio=[j for i in range(audio.index(a)+1,len(audio)) for j in audio[i]]
    for value in a:
        for k in rest_audio:
            merge(value,k)

def merge(y1,y2):
   
    sound1 = AudioSegment.from_file(y1)
    sound2 = AudioSegment.from_file(y2)
    combined = sound1.overlay(sound2)
    combined.export('combined.wav', format='wav')