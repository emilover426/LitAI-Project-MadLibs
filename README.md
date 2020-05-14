# LitAI-Project-MadLibs

## Collaborators
- Andrew Popadics (ajp2245)
- Emily Hao (esh2160)

## Files Submitted
- README.md
- madlibs.py
- story template files (story_template_1.txt, story_template_2.txt)
- word bank files (word_bank_1.csv, word_bank_2.csv)

## Prerequisites
- Python3
- Pandas

## Run Instructions

 Run the following command in the directory containing the files.

 ```python madlibs.py```

 Or, if your default python is Python 2.7:

```python3 madlibs.py```

When prompted, enter the number of the story template you want to use.
Currently, the options are 1 or 2.

## Program Description

`madlibs.py` reads in a story template, detects the keys that need to be replaced, selects a random word for that key from the corresponding word bank, and then replaces the key with that word. If a word has already been selected for that key, or if that key is dependent on a previous key, then the program will find the appropriate word such that the story remains consistent. The program outputs a "randomly" generated story, as well as writes that story to a time-stamped file in a folder named `logs`. The program automatically creates a `logs` folder if one does not already exist.

The story templates are `.txt` files. The "blanks" are of the form `(key)`. The word banks are .csv files. Each key has a column that contains eligible words. If you want to add your own story template and word bank, then create files named `story_template_#.txt` and `word_bank_#.csv`, where `#` is replaced by a number > 2. When prompted, simply enter the number of your new files. Your files should follow the format of the provided story templates and word banks. 
