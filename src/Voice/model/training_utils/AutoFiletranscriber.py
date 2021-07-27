from json import loads
from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave
from tqdm import tqdm
import sys
SetLogLevel(-1)
modelpath = sys.argv[0]
model = Model(modelpath)
if not os.path.exists(modelpath):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)


def transcriber(wavepath):
    wf = wave.open(wavepath, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)
    rec = KaldiRecognizer(model, wf.getframerate())
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            finalresult = rec.FinalResult()
            print(os.path.basename(wavepath).replace(".wav","").replace(" ","_")+"|"+loads(rec.FinalResult())['text'])
            #print(rec.Result())
    sum = 0
    confcounter = 0
    finalresult = rec.FinalResult()
    for i in loads(finalresult)['result']:
        sum = sum + i['conf']
        confcounter+=1
        


    print(os.path.basename(wavepath).replace(".wav","").replace(" ","_")+"|"+loads(finalresult)['text']+"|"+str(sum/confcounter))




def filescheck(directory):
    counter=0
    import os

    for subdir, dirs, files in os.walk(directory):
        for file in tqdm(files):
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".wav"):
                transcriber(str(filepath))
            elif counter==4:
                break
            else:
                counter+=1


filescheck(sys.argv[1])