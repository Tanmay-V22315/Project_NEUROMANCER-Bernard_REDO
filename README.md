## Moved to [Gitlab](https://gitlab.com/Tanmay-V22315/Project_NEUROMANCER-Bernard_REDO)
# Project_NEUROMANCER-Bernard_REDO
 
 
 Remaking Project NEUROMANCER after realizing the original was hopelessly jumbled and archaic and beyond the point of salvation/fixing.

 Look at: [src](./src/README.md) for info


To install:
```bash
git clone (stand-in link)
cd (repo-name) 
make 
```
This will handle all of the installation stuff for you, including the dependencies. If you want to compile the Rust code on a custom platform, you can do that too with the flag `--compile-all` <!-- TODO -->

Directories structure:
*(as of 25/07/2021)*
```
.
├── credits_and_sources
│   ├── people.txt
│   └── websites.txt
├── LICENSE
├── MakeFile
├── README.md
├── setup
│   └── requirements.txt
└── src
    ├── ASR
    │   ├── model
    │   └── STT.py
    ├── NLG
    │   ├── __init__.py
    │   └── mods
    ├── NLP
    ├── README.md
    ├── utils
    └── Voice
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

14 directories, 21 files

```
