# coding: utf-8
import markovify
import glob
from numpy import random
from googletrans import Translator

# randomly sample from sources.
sourcelist = []
sourcelist_sample = []

for filename in glob.glob('data/*.txt'):
    sourcelist.append(filename)

sample_sourcenumber = random.randint(4, 15)
sourcelist_sample = random.choice(sourcelist, sample_sourcenumber)


def print_sources():
    sourcelist_sample_toprint = list(sourcelist_sample)
    sourcelist_sample_toprint = [s.strip('datatxt').replace('_', ' ').replace('/', '').replace('.', '') for s in sourcelist_sample_toprint]   # noqa: E501
    print ' + '.join(sourcelist_sample_toprint) + ':' + '\n'


# get raw text as string; build sampled models.
markoved_texts = []

for s in sourcelist_sample:
    with open(str(s)) as f:
        text_model = markovify.Text(f)
        markoved_texts.append(text_model)

# build the composite model.
lipsum_model = markovify.combine(markoved_texts)

n_sent = random.randint(8, 12)
sent_chain = []

for i in range(n_sent):
    sent_chain.append(lipsum_model.make_sentence())

en_text = ' '.join(sent_chain)

# translate to latin.
translator = Translator()
translation = translator.translate(en_text, dest='la')
la_text = translation.text


# print english text and latin text.
def print_texts():
    print en_text
    print '<-->'
    print la_text


# to do: replace untranslatable words with 'lorem'. to do so: convert to array...run all through '.detect' command...if not 'latin', replace with 'lorem'   # noqa: E501
print_sources()
print_texts()
