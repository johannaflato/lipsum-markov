# coding: utf-8
import csv
import markovify
import glob
import random
from googletrans import Translator

"""
TO DO: save everything as a list of dicts:
each iteration (key) has SOURCE: ex, EN_TEXT: ex, LA_TEXT: ex

"""
# randomly sample from sources.
sourcelist = []
all_iterations = []
n_iterations = 10

for filename in glob.glob('data/*.txt'):
    sourcelist.append(filename)


def lipsum_generate():
    for iteration in range(n_iterations):
        n_sources = random.randint(1, 30)
        sourcelist_sample = []
        sourcelist_sample = random.sample(sourcelist, n_sources)    # randomly sample from sources  # noqa: E501

        def joined_sources():
            sourcelist_sample_toprint = list(sourcelist_sample)
            sourcelist_sample_toprint = [s.strip('datatxt').replace('_', ' ').replace('/', '').replace('.', '') for s in sourcelist_sample_toprint]   # noqa: E501
            return ' + '.join(sourcelist_sample_toprint)     # REMOVED for csv/book: + ':' + '\n'   # noqa: E501

        sources = joined_sources()

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

        # zip dictionary from generated texts; append to mega list
        keys = ["sources", "en_text", "la_text"]
        values = [sources, en_text, la_text]
        new_text_pairs = dict(zip(keys, values))
        all_iterations.append(new_text_pairs)


lipsum_generate()

# write iterations to csv
with open('results/lipsum_book2.csv', 'w') as csvfile:
    fieldnames = ["sources", "en_text", "la_text"]
    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    write.writeheader()
    write.writerows(all_iterations)
