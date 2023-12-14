import Summarize as Summ
import pandas as pd
import numpy as np


txt = pd.read_table('text.txt',header=None,delimiter=None)[0].to_list()
# print(txt)
full_text = ""
for lines in txt:
    full_text += lines

# print(full_text)
summ = Summ.Summarize(full_text)
summarized = summ.summarize(0.7)
print(summarized)
