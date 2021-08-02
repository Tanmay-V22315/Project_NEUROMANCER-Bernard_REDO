import sys
import hjson
import os

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



def modProcessor(mode, modifiable):
    print("modProcessor() is being called")
    for (root,dirs,files) in os.walk(directoryOfThisFile+'/SSMLmods', topdown=True):
        sys.path.append(root)
        if files!=[]:
            if files[files.index("config.hjson")]:
                config = hjson.load(open(root+"/config.hjson"))
                if mode=="direct":
                    return directModProcessor(modifiable, config['tagStart'],config['tagEnd'],config['fileNameToBeExecuted'])
                    


def directModProcessor(processedList: list, tagStart, tagEnd, fileName):
    
    for chunkOfSentence in processedList:
        if tagStart in chunkOfSentence and type(chunkOfSentence)==str:
            assert tagEnd in chunkOfSentence, tagStart+" was not closed with "+tagEnd
            chunkOfSentenceInBetween = getTextInBetween(inputtext=chunkOfSentence,tagstart=tagStart, tagend=tagEnd)
            exec("import "+fileName)
            #Example this is what a gobbledegookynatorifier sounds like <media>/home/randomaccessvemuri/Downloads/output.wav</media> . Sounds interesting, doesn't it?
            indexOfChunk = processedList.index(chunkOfSentence) 
            modOutput = eval(fileName+".main(chunkOfSentenceInBetween)")
            processedList[indexOfChunk:indexOfChunk+1]=chunkOfSentence[0:chunkOfSentence.index(tagStart)], modOutput, chunkOfSentence[chunkOfSentence.index(tagEnd)+len(tagEnd):]

    print(processedList)
    return processedList



