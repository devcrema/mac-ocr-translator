from pprint import pformat

import pysle.isletool


def get_pronunciation(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        try:
            result += word + ": " + pformat(pysle.isletool.LexicalTool().lookup(word)[0][0][0]) + "\n"
        except:
            pass
    return result
