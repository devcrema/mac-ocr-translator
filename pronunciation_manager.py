import asyncio

import pysle.isletool

# TODO 비동기로 동작하도록 구현하고 연동하기
async def get_pronunciation_by_word(word: str) -> str:
    return word + ": " + "".join(pysle.isletool.LexicalTool().lookup(word)[0][0][0][0]) + "\n"


async def get_pronunciation_async(sentence):
    words = sentence.split(" ")
    for word in words:
        try:
            pronunciations = await get_pronunciation_by_word(word)
            print(pronunciations)
        except:
            pass


def get_pronunciation(sentence: str) -> str:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_pronunciation_async(sentence))
    loop.close()


get_pronunciation("this is just testing for the record asd")
