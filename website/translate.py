import googletrans
import textblob

languages = googletrans.LANGUAGES


def translate_it(text, input_lang, output_lang='hindi'):
    try:
        for key, value in languages.items():
            if (value == input_lang):
                from_language_key = key
        # Get the To Language key
        for key, value in languages.items():
            if (value == output_lang):
                to_language_key = key

        # Turn Original Text to a TextBlob
        words = textblob.TextBlob(text)

        # Translate Text
        words = words.translate(
            from_lang=from_language_key, to=to_language_key)
    except:
        pass
    return words
