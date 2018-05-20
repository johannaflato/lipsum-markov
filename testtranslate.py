# coding: utf-8

from googletrans import Translator

translator = Translator()
translation = translator.translate('Pain of itself because it is pain, but because occasionally circumstances occur in which toil and pain...', dest='la')
la_text = translation.text

print la_text
