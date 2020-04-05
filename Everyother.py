import numpy as np
import pandas as pd


meme = np.arange(88)
meme = meme.tolist()

for i in meme:
    if i % 2 == 0:
        meme.remove(i)
    elif i % 2 == 0:
        continue

meme = meme[0::2]
final = "There are {} Questions on this assignment \n{}"
print(final.format(len(meme), meme))

#improvements
#(start,stop,step)
np.arange(1,85,4)
