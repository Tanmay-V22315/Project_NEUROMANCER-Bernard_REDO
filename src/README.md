 
# <u> Project-NEUROMANCER: An end-to-end digital assistant framework  </u>

### <u>Introduction:</u>
So, this is a redo of the previous [**Project NEUROMANCER**](https://github.com/Tanmay-V22315/Project-NEUROMANCER) (formerly **BRIGHTNICK7000**). **That** was *scrapped* due to archaic, terrible, absolutely horrendous and bodgy code management. 
As Henry Ford has said: 
> The only real mistake is the one from which we learn nothing.
> -Henry Ford


In that step, the following *"corrections"* have been made


**<u>Having learnt from past mistakes:</u>**
- Modules and code have been categorically divided to make stuff easier to understand and edit.
- Syntax usage has been improved, I had made some rather stupid decisions earlier, and those have been rectified. (for example, For referencing jokes  a CSV file, I was calling `shuf` using `os.system()` and then creating a seperate file for getting one of the lines......point is, it was terrible) 
- I have, well, *discovered*, for the lack of a better term, a newer, more....*robust* method for user intent-classification through which I hope to increase the accuracy of the whole thing while also more comfortably handling various categories of inputs.
- Made the whole project more modular, with support for community mods while making it easier to make them (if that ever happens, that is) and making it generally easier to adopt this project for personal/business purposes. (unlikely but still..)
- Latex PDF documentation will be out soon, once I am actually done with the project (Come on, I'm, like, the only person working on this project).
- Made better use of Rust for speed-up in certain places 
- A new TTS model (Thanks to [Coqui TTS](https://github.com/coqui-ai/TTS)), ditching the older *"Proof-Of-Concept"* Cortana version, which used tacotron2, which from my "research", is slower than Glow-TTS. (Also it doesn't sound that good)
- A more user-friendly and understandable config file.
- Take heed regarding licensing stuff. (I didn't get into any trouble last time, but just to stay safe)
- Handle Directories better


 ## Granular Roadmap:
 **Moved to Github Projects**


 ## Devlogs:

Here you can see my sanity waning.....and also see me finding out about some cool stuff along the way:

> ### TTS
> - Development has started, As of now, stuff is pretty straight-forward in TTS so I'll probably finish the model deployment part in a day or two (I've got school too, y'know). The biggest PITA is actually training the model for which I have yet to transcribe the audio files, which itself might take a few days or maybe even a few weeks. Fortunately, given that the voice that I'm transcribing is from a game, wikis and fandoms will help me out here which is pretty neat.
> - The TTS versions are starting to become a *bit* of a problem. My current models don't work in the newer version due to some issues with phonemization or something so I'll have to revert to the old version (v0.0.13 )
> - I had to rename the TTS folder because my dumbass didn't realise that that could cause conflicts with the actual Coqui TTS package.
> - While lurking in Coqui TTS repositories' Issues tab, I found out about [SSML](https://cloud.google.com/text-to-speech/docs/ssml) so ig we're working on that now 
> - Keval Shah (a class-mate) has started working on the project as a collaborator.
> - (25/7/2021) Just replaced Pop!OS with Manjaro on my laptop, lost all of my stuff in the process (except my code and other stuff, besides I had made a backup of the entire /home directory so I'm safe anyway). Sorting things out, shouldn't take too long.
> - I'm going to include the option to choose between the Debian installation process (as you can tell, for Debian-based distros) and Arch installation process during the `make` command.....you get the idea
> - Introducing support for mods, starting with SSML.
