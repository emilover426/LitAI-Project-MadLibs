import sys
import os
import string
import time
import re
import pandas as pd
import random

t = time.time()

### Make a logs folder if one doesn't exist.
if not os.path.isdir('logs'):
    print('Made a logs folder')
    os.mkdir('logs')


###print function and log function (writes to log/time_output_file if specified)
def log(x, t, print2screen=False, output_file =None):
    if print2screen: print(x)
    if output_file:
        with open("logs/"+str(t)+ "_" +output_file, 'a+') as ofile:
            ofile.write(x+'\n')


### Fill in template with random words from word bank
def fillin_template(template_file, word_table, story_num):
    file = open(template_file + str(story_num)+ ".txt", "r")
    var_dict = {}
    for line in file:
        keys = [str(s) for s in re.findall('\(([^)]+)', line)]
        new_line = line
        for k in keys:
            if k[-1] == '*':
                temp_k = k[:-1]
            else:
                temp_k = k
            col = word_table[temp_k]
            if re.search('[a-z]', temp_k):
                i = re.search('[a-z]', temp_k).start()
                if temp_k[:i] in var_dict:
                    index = var_dict[temp_k[:i]]
                    word = col.iloc[index]
            elif temp_k in var_dict:
                index = var_dict[temp_k]
                word = col.iloc[index]
            else:
                while True:
                    random_index = random.randint(0,len(col)-1)
                    word = col.iloc[random_index]
                    if pd.notna(word):
                        var_dict[temp_k] = random_index
                        break
            if temp_k != k:
                word = word.capitalize()
            new_line = new_line.replace("("+k+")","("+word+")")

        if new_line != "":
            log(new_line,t,print2screen=True,output_file=str(story_num))

    file.close()
    return


log("Welcome to Mad Libs!", t, print2screen=True)
log("Pick a story number: ", t, print2screen=True)
story_num = int(input())

log("You selected story #" + str(story_num) + ".",t,print2screen=True)

word_bank = pd.read_csv("word_bank_"+str(story_num)+".csv")

log(" ", t, print2screen=True)
log("Your story is: ", t, print2screen=True)
log(" ", t, print2screen=True)
fillin_template("story_template_", word_bank, story_num)
