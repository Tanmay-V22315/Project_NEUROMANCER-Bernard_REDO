# TTS Training utils

Stuff in this folder is meant to make training a TTS model less of a pain in the ass. 
The python notebooks are meant to be run on [Colab](https://colab.research.google.com/)
## Actual training stuff
My recommendation is: 
1. First use LjSpeechTrainer.ipynb so that you can make use of the huge number of audio files in the LjSpeech dataset. 
2. Then fine-tune the TTS model you trained with the LjSpeech dataset with your own custom dataset, making good use of previous knowledge the model gained from the giant LjSpeech dataset while also getting a nice-ish sounding TTS model. (sort of like a song remix, except that you will get the voice of.....you get the idea)

## Pre-processing stuff

There's an autotranscriber which you can use to generate a CSV file of your own dataset. It makes use of Kaldi and vosk so you need those to be built and installed.

Autotranscriber Usage (Assuming you have all the requirements):

```bash
#Do this in the terminal
#The order of arguments is extremely important
# Stuff in curly braces are the arguments that you have to change
python3 dir/to/AutoFiletranscriber.py {directory/to/ASR model} {directory/of/.wav files}\
 > {directory of csv file (a new one will be created if the file doesn't exist)}
 ```
 If you don't have a model (..Odd...) you can download one according to your dataset from [here.](https://alphacephei.com/vosk/models)

 While this does work to some extent, you will still have to manually go in and fix the punctuations and casing while also looking out for some mistakes that the model may have made.
 I've made the work a *little* easier by making a `confidence` column. So when you sit down and think of having to parse through hundreds, maybe even thousands of sentences, you can rest a *bit* easy that I have done a bit of work for you. Open the CSV in Excel (or your favourite spreadsheet app), mark the cells as red, green or yellow based on confidence score and then work on fixing the ones with lower confidence as those will most probably have issues.