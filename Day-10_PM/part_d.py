from typing import Dict


def analyze_text(text: str, **options) -> Dict:

    result = {}

    words = text.split()

    if options.get("count_words", True):
        result["word_count"] = len(words)

    if options.get("count_sentences", True):
        result["sentence_count"] = text.count(".") + text.count("!") + text.count("?")

    if options.get("find_longest_word", True):
        result["longest_word"] = max(words, key=len)

    if options.get("sentiment_simple", True):

        positive = ["good", "great", "excellent"]
        negative = ["bad", "poor", "terrible"]

        score = 0

        for w in words:
            if w.lower() in positive:
                score += 1
            if w.lower() in negative:
                score -= 1

        result["sentiment_score"] = score

    return result


text = "Python is a great language. It is good for AI."

print(analyze_text(text))