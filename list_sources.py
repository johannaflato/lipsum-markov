import glob
from numpy import random

# to write text file instead of returning a dictionary:
# data = glob.glob('data/*.txt')
# with open("sources.txt", "w") as sources:
#    for eachsource in data:
#        sources.write((eachsource.strip('data/txt').replace("_", " ").replace(".", ""))+'\n')   # noqa: E501

sourcelist = []
sourcelist_sample = []

for filename in glob.glob('data/*.txt'):
    sourcelist.append(filename.strip('data/txt').replace("_", " ").replace(".", ""))   # noqa: E501

print sourcelist

sourcelist_sample = random.choice(sourcelist, 5)

print sourcelist_sample
