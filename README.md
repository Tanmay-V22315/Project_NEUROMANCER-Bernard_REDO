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
```
├── LICENSE
├── MakeFile
├── README.md
├── setup
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
        ├── model
        │   ├── config.json
        │   └── model_file.pth.tar
        ├── __pycache__
        │   └── TTS.cpython-38.pyc
        ├── README.md
        ├── resources.json
        └── voice.py

11 directories, 12 files
```