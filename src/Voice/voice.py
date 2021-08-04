#     ██╗
#  ██╗╚██╗
#  ╚═╝ ██║
#  ▄█╗ ██║
#  ▀═╝██╔╝
#     ╚═╝

#  Written by Tanmay Vemuri
#  ___ ___ __ 
#   |   | (_  
#   |   | __) 
            

#importing and setting up some stuff

import time
import warnings
import sounddevice as sd
from TTS.utils.synthesizer import Synthesizer
import hjson
import numpy as np
import os
import sys
from utils.SSMLPostprocessor import Txtpreprocessor, pauseProcessor, modProcessor

fileDir = os.path.dirname(os.path.realpath(__file__))

chars = hjson.load(open(fileDir+"/resources.json"))
#Model name and config file name should be corresponding with the paramters called in the function (Otherwise you're free to edit the code but I doubt it will be pleasant down the road)
synthesizer = Synthesizer(fileDir+"/model/model_file.pth.tar", fileDir+"/model/config.json", None, None, True) 
sample_rate=hjson.load(open(fileDir+"/model/config.json"))["audio"]["sample_rate"]

from nltk.tokenize import RegexpTokenizer
  
tokenizer = RegexpTokenizer("""[A-Za-z0-9 _.,!?"@#'/$]*""")



#----------------------------------------------------------------------------------------------------------------------------------------#
#Nifty stuff taken from https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print#:~:text=If%20you%20don't%20want,the%20top%20of%20the%20file.
def blockPrint(mode2="release"):
    if mode2=="release":
        sys.stdout = open(os.devnull, 'w')
    else:
        pass

# Restore
def enablePrint(mode2="release"):
    if mode2=="release":
        sys.stdout = sys.__stdout__
    else:
        pass
#----------------------------------------------------------------------------------------------------------------------------------------#



def speak(cleanedText: str, mode: str="release", samplerate=sample_rate):
    blockPrint(mode)
    wav = synthesizer.tts(cleanedText) #Generate a list with the frequencies. You'll have to mess about with the source code if you want to use a multispeaker model. Since that isn't a realistic need, I didn't really bother with it.
    enablePrint(mode)
    sd.play(modProcessor("audio", np.array(wav)), samplerate) #Play the actual audio
    time.sleep(len(wav)/samplerate) #Derive the time duration of the audio to be played by dividing the number of elements in the list by the sample rate. (ngl, I didn't think this would work, not this well anyway)
    sd.stop()


def cleanspeak(inputtext="Some error has occured.", mode="release"): #Sorry for the ominous/weird name. What I mean with the name is to clean up the input text and then speak. This is pretty important because in certain cases, in input text you might see stuff like ".." or something and that *will* f*** with the text-to-speech, causing an unnecessary/unexpected failure.
    
    if mode=="debug":
        print("In debugging mode")

    time1 = time.perf_counter()
       

    fintext = inputtext #preserve input for future purposes (i.e. debugging stuff)
    
    
    if "<pause>" in fintext:
        fintext =pauseProcessor(Txtpreprocessor(modProcessor("replacement", fintext)))
    else:
        fintext =Txtpreprocessor(modProcessor("replacement", fintext))
    
    
    if type(fintext)!=list:
        fintext = [fintext]

    #The comments in the following for-loop is only for "direct" mods
    for chunk in modProcessor("direct",fintext):     
        if type(chunk)==float:
            #return a float if you wish the speaker to stop for sometime during mod.
            time.sleep(chunk)
        elif type(chunk)==list:
            #if you wish to play an audio file or just any array of audio signals through mods, you have to return a list with the first element being the signal array and the second element being the sample rate. You also have to set the mod type in your mod's hjson file to "direct"
            sd.play(chunk[0], chunk[1])
            time.sleep(len(chunk[0])/chunk[1])
            sd.stop()
        elif chunk=='':
            warnings.warn("Empty string was passed to TTS")
        else:
            print(chunk)
            speak(textCleanupandFormatting(chunk), mode)
    
    


    time2 = time.perf_counter()
    if mode=="debug":
        print("DEBUG INFO: ")
        print("=============")
        print("\nText as seen by the TTS model: ")
        print(fintext)
        print("Time taken for sentence: "+inputtext+" is "+ str(time2-time1))
        print("Avg. Time per word= "+ str((time2-time1)/len(tokenizer.tokenize(inputtext))) )
        print("Sample Rate: "+str(sample_rate)+"\n")







def textCleanupandFormatting(textToBeCleanedUp):
    if textToBeCleanedUp!='':
        textToBeCleanedUp = tokenizer.tokenize(textToBeCleanedUp)
        for i in chars["aexpansions"].keys():
            if i in textToBeCleanedUp:
                textToBeCleanedUp[textToBeCleanedUp.index(i)]=chars["aexpansions"][i]

        for i in chars["slangs"].keys():
            if i in textToBeCleanedUp:
                textToBeCleanedUp[textToBeCleanedUp.index(i)]=chars["slangs"][i]

        textToBeCleanedUp = " ".join(textToBeCleanedUp)
        
        for i in chars['problemchars'].keys():
            if i in textToBeCleanedUp:
                textToBeCleanedUp = textToBeCleanedUp.replace(i, chars['problemchars'][i])

        if textToBeCleanedUp.strip()[-1] not in [".", "?", "!", ";", ","]:
            textToBeCleanedUp = textToBeCleanedUp+"."
        return textToBeCleanedUp
    else:
        warnings.warn("Empty string was passed to TTS")
        return ''