#TODO: create a python program that generates requirements.txt for all mods.
import os
import soundfile as sf

#Test Sentence: This is what a gobbldygookinatorifier sounds like in action <media> /path/to/ggktfr.wav </media>
def main(textBetweenSpecifiedTags):
    assert os.path.isfile(textBetweenSpecifiedTags.strip()), "Incorrect audio file directory: "+textBetweenSpecifiedTags
    data, sr = sf.read(textBetweenSpecifiedTags.strip())
    return [data, sr]

    

