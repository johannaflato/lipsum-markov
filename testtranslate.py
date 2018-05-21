# coding: utf-8

from googletrans import Translator

translator = Translator()
translation = translator.translate('Pain of alkdflkg because it is pain, but because occasionally circumstances occur in which toil and pain...', dest='la')   # noqa: E501
la_text = translation.text

print la_text

# to do: replace untranslatable words with 'lorem'.

# to do so: convert to array...
# run all through '.detect' command...
# if not 'latin', replace with 'lorem'   # noqa: E501

# for word in translation:
#    if word.detect() =! lang=la:
#        word.replace(lorem)
