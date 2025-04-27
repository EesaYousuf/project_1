# from googletrans import Translator
# Translator=Translator()
# txt='comment allez vous?'
# out_put=Translator.Translatate(txt,dest='en')
# print(out_put.text)
# from googletrans import Translator

# # Create an instance of Translator
# translator = Translator()

# # Text to be translated
# txt = 'comment allez vous?'

# # Translate the text to English
# out_put = translator.translate(txt, dest='en')

# # Print the translated text
# print(out_put.text)
import asyncio
from googletrans import Translator

async def main():
    # Create an instance of Translator
    translator = Translator()

    # Text to be translated
    txt = 'mai kuch nhi smghti hu?'

    # Translate the text to English
    out_put = await translator.translate(txt, dest='en')

    # Print the translated text
    print(out_put.text)
    # Run the main function
asyncio.run(main())

