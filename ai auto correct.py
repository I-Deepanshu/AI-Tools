import Levenshtein
from collections import Counter

# Enhanced list of words for our dictionary
dictionary = [
    "apple", "banana", "orange", "grape", "kiwi", "mango", "peach", "pear", "pineapple",
    "strawberry", "watermelon", "blueberry", "raspberry", "blackberry", "cherry",
    "apricot", "plum", "lemon", "lime", "coconut", "papaya", "guava", "pomegranate",
    "dragonfruit", "fig", "avocado", "melon", "cranberry", "passionfruit", "nectarine",
    "kiwifruit", "tangerine", "cantaloupe", "lychee", "persimmon", "grapefruit", "date",
    "boysenberry", "durian", "kiwano", "mangosteen", "mulberry", "quince", "rhubarb",
    "starfruit", "soursop", "jackfruit", "loquat", "blackcurrant", "elderberry",
    "book", "pen", "pencil", "notebook", "computer", "keyboard", "mouse", "monitor",
    "table", "chair", "lamp", "clock", "bed", "sofa", "television", "microwave",
    "car", "bicycle", "motorcycle", "airplane", "train", "bus", "boat", "subway",
    "guitar", "piano", "violin", "trumpet", "flute", "drums", "saxophone", "accordion",
    "coffee", "tea", "juice", "water", "soda", "wine", "beer", "cocktail",
    "dog", "cat", "bird", "fish", "rabbit", "hamster", "turtle", "horse",
    "sun", "moon", "star", "cloud", "rain", "snow", "wind", "thunder"
]

def get_nearest_word(word, dictionary):
    distances = [Levenshtein.distance(word, dict_word) for dict_word in dictionary]
    min_distance = min(distances)
    nearest_words = [dictionary[i] for i, distance in enumerate(distances) if distance == min_distance]
    return nearest_words

def auto_correct(input_text, dictionary):
    words = input_text.split()
    corrected_text = []
    for word in words:
        nearest_words = get_nearest_word(word, dictionary)
        corrected_text.append(nearest_words[0])  # Choose the first nearest word as the correction
    return " ".join(corrected_text)

# Allow user input for the text to correct
user_input = input("Enter a sentence: ")
corrected_text = auto_correct(user_input, dictionary)
print("Corrected text:", corrected_text)
