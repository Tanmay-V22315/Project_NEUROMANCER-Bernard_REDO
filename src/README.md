 
# <u> Project NEUROMANCER </u>

### <u>Introduction:</u>
So, this is a redo of the previous **Project NEUROMANCER** (formerly **BRIGHTNICK7000**). **That** was *scrapped* due to archaic, terrible, absolutely horrendous and bodgy code management. 

**<u>Having learnt from past mistakes:</u>**
- Modules and code have been categorically divided to make stuff easier to understand and edit.
- Syntax usage has been improved, I had made some rather stupid decisions earlier, and those have been rectified. (for example, For referencing jokes  a CSV file, I was calling 'shuf' using os.system() and then creating a seperate file for getting one of the lines......point is, it was terrible) 
- I have, well, *discovered*, for the lack of a better term, a newer more....*robust* method for user intent-classification through which I hope to increase the accuracy of the whole thing while also more comfortably handling various categories of inputs.
- Made the whole project more modular, with support for community mods while making it easier to make them (if that ever happens, that is) and making it generally easier to adopt this project for personal/business purposes. (unlikely but still..)
- Latex PDF documentation will be out soon, once I am actually done with the project (Come on, I'm, like, the only person working on this project).
- Made better use of Rust for speed-up in certain places (or maybe Zig, certainly not C++ 'cause f*** C++)
- A new TTS model (Thanks to [Coqui TTS](https://github.com/coqui-ai/TTS)), ditching the older "Proof-Of-Concept" Cortana version, which used tacotron2, which from my "research", is slower than Glow-TTS .
- Understandable Config file.