import sys
import hjson
import os
import numpy as np
import warnings


directoryOfThisFile = os.path.dirname(os.path.realpath(__file__))

def getTextInBetween(inputtext, tagstart, tagend):
    return inputtext[inputtext.index(tagstart)+len(tagstart): inputtext.index(tagend)]




#The somewhat "Recursive" function will break automatically if no more tags are found, so don't worry about hitting max recursion depth....unless it does happen in which case, please let me know
def Txtpreprocessor(inputstring):
        
    #Alias tag encloses a dictionary which can be used for replacements and stuff.
    if "<alias>" in inputstring:
        assert "</alias>" in inputstring, "<alias> tag was not closed with </alias>"
        try:
            aliasdict = eval(inputstring[inputstring.index("<alias>")+len("<alias")+1:inputstring.index("</alias>")])
        except:
            return "Something is wrong with the alias specification. Make sure that tags only enclose the dictionary."
        inputstring = inputstring[inputstring.index("</alias>")+len("</alias>")+1:]
        for i in aliasdict.keys():
            inputstring = inputstring.replace(i,aliasdict[i])

        return Txtpreprocessor(inputstring)



    # Spell-it tag will (as the name implies) spell out the word, basically "SSML" will be converted to "S S M L", "World" will become "W o r l d".
    elif "<spell-it>" in inputstring:
        assert "</spell-it>" in inputstring, "<spell-it> tag was not closed with </spell-it>"
        # This incantation, while pretty unreadable, does the job of finding text between the tags and inserting spaces between the characters (the same function is being called so that it can be recursively done, thus dealing with multiple instances of the tag). A more readable version is written in the comments just below
        inputstring = inputstring.replace("<spell-it>"+getTextInBetween(inputstring, "<spell-it>", "</spell-it>")+"</spell-it>", " ".join(list(getTextInBetween(inputstring, "<spell-it>", "</spell-it>"))) )
        
        
        #SAME-AS
        # textInBetweenTags = inputstring[inputstring.index("<spell-it>")+len("<spell-it>"): inputstring.index("</spell-it>")]
        # replacee = "<spell-it>"+textInBetweenTags+"</spell-it>"
        # textToBeReplaced = " ".join(list(textInBetweenTags))
        # inputstring = inputstring.replace(replacee)
        
        
        return Txtpreprocessor(inputstring)


    else:
        if inputstring==None:
            return "Some error has occured."
        else:
            return inputstring




def pauseProcessor(inputstring):
    proccache=[inputstring]
    responselist = []
    for _ in range(0,inputstring.count("<pause>")):
        toBeProcessed = proccache[-1]
        try:
            duration = float(getTextInBetween(toBeProcessed, "<pause>", "</pause>").replace(" ",""))
            beginningChunk=toBeProcessed[0:toBeProcessed.index("<pause>")]
            endingChunk=toBeProcessed[toBeProcessed.index("</pause>")+len("</pause>"):]
            responselist.append(beginningChunk)
            responselist.append(duration)
            if "<pause>" not in endingChunk:
                responselist.append(endingChunk)
            else:
                proccache.append(endingChunk)

        except ValueError:
            print("FATAL: <pause> request contained non-integer characters, exiting....")
            print("=====\n")
            print("DEBUG INFO: ")
            print("=========== \n")
            print("The complete input string was: "+str(inputstring))
            print("The problematic <pause> request was: "+str(getTextInBetween(inputstring, "<pause>", "</pause>").replace(" ","")))
            sys.exit()
    
    return responselist

#This is not the best solution, but due to lack of time, I do not wish to dwell on this any longer.
#TODO: Fix this 
def modProcessor(mode, modifiable):
    for item in os.listdir(directoryOfThisFile+"/SSMLmods"):
        directoryOfMod=directoryOfThisFile+"/SSMLmods/"+item
    
        if directoryOfMod not in sys.path:
            sys.path.append(directoryOfMod)

        if "config.hjson" in os.listdir(directoryOfMod):
            modConfig = hjson.load(open(directoryOfMod+"/config.hjson"))
        if modConfig['shouldExecute'] is True:
            if modConfig['isModExperimental']==True:
                warnings.warn("This mod ("+modConfig["modName"]+") has been marked as Experimental. Use at your own risk. To disable this mod, use pNpm or set 'shouldExecute' in the mod's config.json to false.")

            if modConfig['type']==mode and mode=="replacement":
                return replacementModProcessor(modifiable, modConfig['tagStart'], modConfig['tagEnd'], modConfig['fileNameToBeExecuted'])
            elif modConfig['type']==mode and mode=="direct":
                return directModProcessor(modifiable, modConfig['tagStart'], modConfig['tagEnd'],modConfig['fileNameToBeExecuted'])
            elif modConfig['type']==mode and mode=="audio":
                return audioModProcessor(modifiable, modConfig['fileNameToBeExecuted'])
        else:
            return modifiable
                


def directModProcessor(processedList: list, tagStart: str, tagEnd: str, fileName: str):
    for chunkOfSentence in processedList:
        if type(chunkOfSentence)==str and tagStart in chunkOfSentence :
            assert tagEnd in chunkOfSentence, tagStart+" was not closed with "+tagEnd+" (Mod's file name is: "+fileName+")"
            chunkOfSentenceInBetween = getTextInBetween(inputtext=chunkOfSentence,tagstart=tagStart, tagend=tagEnd)
            exec("import "+fileName)
            indexOfChunk = processedList.index(chunkOfSentence) 
            modOutput = eval(fileName+".main(chunkOfSentenceInBetween)")
            processedList[indexOfChunk:indexOfChunk+1]=chunkOfSentence[0:chunkOfSentence.index(tagStart)], modOutput, chunkOfSentence[chunkOfSentence.index(tagEnd)+len(tagEnd):]
    return processedList



def replacementModProcessor(stringinput: str, tagStart: str, tagEnd: str, fileName: str):
    if tagStart in stringinput:
        assert tagEnd in stringinput, tagStart+" was not closed with "+tagEnd
        requiredChunk = getTextInBetween(stringinput, tagStart, tagEnd)
        exec("import "+fileName)
        modOutput = eval(fileName+".main(requiredChunk)")
        stringinput=stringinput.replace(tagStart+requiredChunk+tagEnd, modOutput)
        return stringinput
        
    else:
        return stringinput

def audioModProcessor(audioSignalArray: list, fileName: str) -> list or np.ndarray:
    exec("import "+fileName)
    return eval(fileName+".main(audioSignalArray)")
