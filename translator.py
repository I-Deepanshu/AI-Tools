from googletrans import Translator

def english_to_french_translation(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='fr').text
    return translated_text

def french_to_english_translation(text):
    translator = Translator()
    translated_text = translator.translate(text, src='fr', dest='en').text
    return translated_text

if __name__ == "__main__":
    input_text = input("Enter the text you want to translate: ")

    # Translate English to French
    translated_to_french = english_to_french_translation(input_text)
    print(f"English to French Translation: {translated_to_french}")

    # Translate French to English
    translated_to_english = french_to_english_translation(input_text)
    print(f"French to English Translation: {translated_to_english}")
