import sys 
sys.path.append("./..")
print("Importing voice.py file. First time might take a while.")
#import the voice.py file
import voice


while 1:
    try:
        #Keep the second parameter as debug if you want details regarding inference: 
        voice.cleanspeak(input("What do you want me to say: "), "debug")
    except KeyboardInterrupt:
        print("\n Understood, stopping now....")
        break



