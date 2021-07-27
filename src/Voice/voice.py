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
chars = hjson.load(open(os.path.dirname(os.path.realpath(__file__))+"/resources.json"))
synthesizer = Synthesizer(os.path.dirname(os.path.realpath(__file__))+"/model/model_file.pth.tar", os.path.dirname(os.path.realpath(__file__))+"/model/config.json", None, None, True) #Model name and config file name should be corresponding with the paramters called in the function (Otherwise you're free to edit the code but I doubt it will be pleasant down the road)
sample_rate = 22050

from nltk.tokenize import RegexpTokenizer
  
tokenizer = RegexpTokenizer("""[A-Za-z0-9 _.,!"'/$]*""")



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





def cleanspeak(inputtext="Some error has occured.", mode="release"): #Sorry for the ominous/weird name. What I mean with the name is to clean up the input text and then speak. This is pretty important because in certain cases, in input text you might see stuff like ".." or something and that *will* f*** with the text-to-speech, causing an unnecessary/unexpected failure.
    if mode=="debug":
        print("In debugging mode")
    time1 = time.perf_counter()
    fintext = inputtext
    fintext = tokenizer.tokenize(fintext)
    
    for i in chars["aexpansions"].keys():
        if i in fintext:
            fintext[fintext.index(i)]=chars["aexpansions"][i]
        
    
    
    for i in chars["slangs"].keys():
        if i in fintext:
            fintext[fintext.index(i)]=chars["slangs"][i]
        




    fintext = " ".join(fintext)
    
    #text cleanup:
    
    for i in chars['problemchars'].keys():
        if i in fintext:
            fintext = fintext.replace(i, chars['problemchars'][i])

    if mode=="debug":
        try:
            assert fintext not in [".", "?", "!", ";", ",", "'"]
        except AssertionError:
            print("invalid request: "+fintext)
            return


    if fintext.strip()[-1] not in [".", "?", "!", ";", ","]:
        fintext = fintext+"."

    
    
    print(inputtext) #print the final text (which would be the output from the perspective of NLG)

        

    blockPrint(mode)
    wav = synthesizer.tts(fintext) #Generate a list with the frequencies. You'll have to mess about with the source code if you want to use a multispeaker model. Since that isn't a realistic need, I didn't really bother with it.
    enablePrint(mode)

    sd.play(np.array(wav), sample_rate) #Play the actual audio
    time.sleep(len(wav)/sample_rate) #Derive the time duration of the audio to be played by dividing the number of elements in the list by the sample rate. (ngl, I didn't think this would work, not this well anyway)
    sd.stop()
    time2 = time.perf_counter()
    if mode=="debug":
        print("DEBUG INFO: ")
        print("=============")
        print("\nText as seen by the TTS model: "+fintext)
        print("Time taken for sentence: "+inputtext+" is "+ str(time2-time1))
        print("Avg. Time per word= "+ str((time2-time1)/len(tokenizer.tokenize(fintext))) )
        print("Sample Rate: "+str(sample_rate)+"\n")


