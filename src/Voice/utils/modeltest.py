import sys 
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")
print("Importing and evaluating voice.py file. If this is the first time since startup, this might take a while.")
#import the voice.py file
import voice


while 1:
    try:
        #Keep the second parameter as debug if you want details regarding inference otherwise keep it empty or type "release" (default is "release") 
        voice.cleanspeak(input("What do you want me to say: "), "debug")
    except KeyboardInterrupt:
        print("\nUnderstood, stopping now....")
        break



