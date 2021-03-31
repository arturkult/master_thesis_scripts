from itertools import groupby
from os import listdir

path = './datasets/customized/lub'

a = [name[3:6] for name in listdir(path)]
print([(key, len(list(group))) for key, group in groupby(sorted(a))])


