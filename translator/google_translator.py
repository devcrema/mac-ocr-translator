from googletrans import Translator

translator = Translator()


def translate(text):
    if text:
        return translator.translate(text, src='en', dest='ko').text
    else:
        return ''
