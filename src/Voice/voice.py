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
import sounddevice as sd
from TTS.utils.synthesizer import Synthesizer
import hjson
import numpy as np
import os
import sys
from utils.SSMLPostprocessor import Txtpreprocessor, pauseProcessor

chars = hjson.load(open(os.path.dirname(os.path.realpath(__file__))+"/resources.json"))
#Model name and config file name should be corresponding with the paramters called in the function (Otherwise you're free to edit the code but I doubt it will be pleasant down the road)
synthesizer = Synthesizer(os.path.dirname(os.path.realpath(__file__))+"/model/model_file.pth.tar", os.path.dirname(os.path.realpath(__file__))+"/model/config.json", None, None, True) 
sample_rate = 22050

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



def speak(cleanedText: str, mode: str="release"):
    blockPrint(mode)
    wav = synthesizer.tts(cleanedText) #Generate a list with the frequencies. You'll have to mess about with the source code if you want to use a multispeaker model. Since that isn't a realistic need, I didn't really bother with it.
    enablePrint(mode)
    sd.play(np.array(wav), sample_rate) #Play the actual audio
    time.sleep(len(wav)/sample_rate) #Derive the time duration of the audio to be played by dividing the number of elements in the list by the sample rate. (ngl, I didn't think this would work, not this well anyway)
    sd.stop()


def cleanspeak(inputtext="Some error has occured.", mode="release"): #Sorry for the ominous/weird name. What I mean with the name is to clean up the input text and then speak. This is pretty important because in certain cases, in input text you might see stuff like ".." or something and that *will* f*** with the text-to-speech, causing an unnecessary/unexpected failure.
    if mode=="debug":
        print("In debugging mode")
    time1 = time.perf_counter()
    
    
    fintext = inputtext #preserve input for future purposes (i.e. debugging stuff)

    
    if "<pause>" in fintext:
        fintext =pauseProcessor(Txtpreprocessor(fintext))
    else:
        fintext =Txtpreprocessor(fintext)
    
    
    print(inputtext) #print the final text (which would be the output from the perspective of NLG)
    print(fintext)

    if type(fintext)==list:
        for i in fintext:
           
            if type(i)==float:
                time.sleep(i)
            else:
                speak(textCleanupandFormatting(i), mode)
    else:
        speak(textCleanupandFormatting(fintext))
    


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