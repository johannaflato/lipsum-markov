# coding: utf-8
import markovify
import glob
import random
from googletrans import Translator

# randomly sample from sources.
sourcelist = []
n_loops = 3  # look into altering this to loop endlessly, printing every few minutes.   # noqa: E501

for filename in glob.glob('data/*.txt'):
    sourcelist.append(filename)


def lipsum_generate():
    for iteration in range(n_loops):
        n_sources = random.randint(1, 30)
        sourcelist_sample = []
        sourcelist_sample = random.sample(sourcelist, n_sources)

        def print_iteration():
            print ('ITERATION %s / %s: \n') % (iteration + 1, n_loops)

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
            print en_text + '\n'
            print '<-->' + '\n'
            print la_text + '\n'

        def print_stats():
            print ('(%s sentences generated from %s sources)' % (n_sent, n_sources))   # noqa: E501

        print '\n'
        print_iteration()
        print_sources()
        print_texts()
        print_stats()
        print '\n' + '----'


lipsum_generate()
# consider making functions for 'print,' 'write files/csv,' 'loop on end' etc   # noqa: E501
