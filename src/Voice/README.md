# Text To Speech 

Stuff in this directory is meant for (as the heading implies) Text to Speech. Put the actual TTS model (with the extension: *".pth.tar"*) along with its config.json in the model folder.



Jupyter notebooks regarding training and other utilites have been placed in the model folder as well, within a subdirectory.

If you need any help, have any suggestion, or anything you want to say to me, create a Github issue and I'll look into it. (Same goes for other branches as well)

Here is the directory tree
_(as of 21/07/21)_
```
.
├── model
│   ├── config.json
│   └── model_file.pth.tar
├── README.md
├── resources.json
└── TTS.py

1 directory, 5 files

```
_(tree created with 'tree' util available in linux)_


DISCLAIMER: The code was inspired by the [`synthesize.py` code from Coqui TTS](https://github.com/coqui-ai/TTS/blob/main/TTS/bin/synthesize.py) 



# For the devs:
- Within the directory of this README, you'll find a certain file called `resources.json`. Within that JSON file, you'll find an entry called `problemchars` and within that **there's some *"problematic"* characters which will be converted to their english representation.**
E.g.: `"(hello)"` &#8594; `"bracket open hello bracket close"`
 You can leverage that to mess with the words that the text-to-speech function is getting from NLG. Perhaps stuff like abbreviations for e.x.: `"lol"` &#8594; `"laught out loud"`
 - You *will* have to mess with the source code if you want to use a multi-speaker model.
 - For different languages, you can use something like [M2M-100](https://huggingface.co/transformers/model_doc/m2m_100.html) for translating the input text and replace the TTS model with the a model trained with the language you want. This will add a lot of overhead in terms of time (of course, due to the actual translation) so I didn't bother with it. (Also, I'm surviving on 30 GB of storage on my laptop, I'm running really low so I can't afford to download stuff from here and there.)
- There's a *"patch-work"* support for SSML (Speech Synthesis Markup language) that works by directly messing with the list of floats formed after TTS inference or converting stuff in the input string.
- If you want to test your TTS model, there's a simple `modeltest.py` file within the utils folder which will repeat whatever you type. If you call the actual TTS function as `voice.cleanspeak({sometext here}, "debug")` (i.e if you call the function with "debug" as the second parameter) you will get additional information about the process and stuff, similar to `-v` or `--verbose` as you see pretty often. Look at source code in [voice.py](./voice.py) to understand. 