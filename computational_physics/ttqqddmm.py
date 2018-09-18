import tqdm
from tqdm import tnrange, tqdm_notebook
from time import sleep

pbar=['a', 'b', 'c', 'd']
bar_total=tqdm_notebook(pbar)

for char in bar_total:
    sleep(0.5)
    bar_total.set_description('test: %c'% char)
