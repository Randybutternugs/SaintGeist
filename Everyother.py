import numpy as np
import pandas as pd

#Put the number here and suck mah balls later LOLLL
meme = np.arange(89)
meme = meme.tolist()

for i in meme:
    if i % 2 == 0:
        meme.remove(i)
    elif i % 2 == 0:
        continue

meme = meme[0::2]
final = "There are {} Questions on this assignment \n{}"
print(final.format(len(meme), meme))


##########################===--NEW AND IMPROVED--===#########################################
#improvements
#(start,stop,step)
inp = int(input("last question? "))
#set step to 4 for EOO, 2 for odd
hwl = np.arange(1,inp,4)
np.append(hwl,inp)
hwl
len(hwl)
fefi = "There are {} Questions on this assignment \n{}"
print(fefi.format(len(hwl), hwl))
#hell yes bebey :)))))))
