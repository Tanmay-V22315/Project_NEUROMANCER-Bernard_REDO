# Text To Speech 

Stuff in this directory is meant for (as the heading implies) Text to Speech. Put the actual TTS model (with the extension: *".pth.tar"*) along with its config.json in the model folder.



Jupyter notebooks regarding training and other utilites have been placed in the model folder as well, within a subdirectory.

If you need any help, have any suggestion, or anything you want to say to me, create a Github issue and I'll look into it. (Same goes for other branches as well)

Here is the directory tree
_(as of 25/07/21)_
```

├── installation
│   └── TTSinstallationforArch_based.sh
├── model
│   ├── config.json
│   ├── model_file.pth.tar
│   └── training_utils
│       ├── AutoFiletranscriber.py
│       ├── LjSpeechTrainer.ipynb
│       └── README.md
├── README.md
├── resources.json
├── utils
│   ├── modeltest.py
│   ├── SSMLPostprocessor.py
│   └── SSMLres.json
└── voice.py

4 directories, 12 files


```
_(tree created with 'tree' util available in linux)_


DISCLAIMER: The code was inspired by the [`synthesize.py` code from Coqui TTS](https://github.com/coqui-ai/TTS/blob/main/TTS/bin/synthesize.py) 



# For the devs:
- Within the directory of this README, you'll find a certain file called `resources.json`. Within that JSON file, you'll find an entry called `problemchars` and within that **there's some *"problematic"* characters which will be converted to their english representation.**
E.g.: `"(hello)"` &#8594; `"bracket open hello bracket close"`
 You can leverage that to mess with the words that the text-to-speech function is getting from NLG. Perhaps stuff like abbreviations for e.x.: `"lol"` &#8594; `"laught out loud"`
 - You *will* have to mess with the source code if you want to use a multi-speaker model.
 - For different languages, you can use something like [M2M-100](https://huggingface.co/transformers/model_doc/m2m_100.html) for translating the input text and replace the TTS model with the a model trained with the language you want. This will add a lot of overhead in terms of time (of course, due to the actual translation) so I didn't bother with it. (Also, I'm surviving on 30 GB of storage on my laptop, I'm running really low so I can't afford to download stuff from here and there.)

 ### SSML
- There's a *"patch-work"* support for SSML (Speech Synthesis Markup language) that works by directly messing with the list of floats formed after TTS inference or converting stuff in the input string.
To use the SSML functionality, you must first realize that the syntax is homegrown and different from the conventional syntax. Owing to that nature, I will explain the tags as well since they can be important.
    - To use something similar to bash aliases, where you type one thing but you actually mean something else ("cls" would be the same as "clear"), you can use the `<alias>` tag. In between the alias tag, you must specify a dictionary form of input within the string.
    Example:
    
    `"<alias>{'W3C':'World Wide Web Consortium', 'W3': 'World Wide Web', 'ISO': 'International standards organisation'} </alias> The W3C is the main ISO for the W3. Founded in 1994 and currently..........in the development of standards for the W3."` 
    <p style="text-align: center;">&#8595;</p> 

     `"The World Wide Web Consortium is the main International standards organisation for the World Wide Web. Founded in 1994 and currently..............in the developments of standards for the World Wide Web"`
    
    - The `<spell-it>` tag will split the phrase enclosed within these tags to its individual characters 
    Example:
    `The word Organization in American English is spelt as: <spell-it>Organization</spell-it>` &#8594; `The word Organization in American English is spelt as: O r g a n i z a t i o n.`
   - `<pause>` tag can be used to have breaks in between sentences. for example `Count to 4 <pause> 4 </pause> Inhale. Count to 4 <pause>4<exhale>` will cause the speaker (TTS model) to wait for 4 seconds twice.
   - NOTE: The dots in between the text means I have truncated the output for the sake of saving characters in this README, in practice you will get the whole sentence with the desired output.
 
### TTS model testing

- If you want to test your TTS model, there's a simple `modeltest.py` file within the utils folder which will repeat whatever you type in voice. If you call the actual TTS function as `voice.cleanspeak({sometext here}, "debug")` (i.e if you call the function with "debug" as the second parameter) you will get additional information about the process and stuff, similar to `-v` or `--verbose` as you see pretty often. Look at source code in [voice.py](./voice.py) to understand. By default, in the modeltest.py, the function is being called with the "debug" parameter, with the function taking input from the user (i.e. you) in an infinite `while` loop that will be broken with `KeyBoardInterrupt`.


### Installer:
The installer is meant to be called during the build process (when `make` is used.). To make things a bit neater and stuff, the entire installation script has been partitioned between sections of code (y'know ASR, NLP, NLG etc.). You can edit the files in `/installation` directory if you need any other dependencies to be installed in *your* version of Project NEUROMANCER. It *would* be a good idea to update both the Arch and Debian install, but not strictly necessary.
